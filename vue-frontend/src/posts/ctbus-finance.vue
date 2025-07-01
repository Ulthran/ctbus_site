<script setup>
import BlogHero from '../components/BlogHero.vue'
const posts = window.posts
const slug = 'ctbus-finance'
const info = posts[slug]
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`CDN_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <p >It's all well and good to keep playing around with the newest technologies; make everything serverless, highly-available, and AI-driven. But sometimes a simple application of a couple really old tools is all you need to get a job done and it's always good to stay in practice with them too.</p>
    <p >I'd been considering potential designs for a personal finance app. Thinking thoughts like: how do I secure automated exports from multiple financial institutions? How do I manage authentication for the database access? Can I do the whole thing serverlessly? After considering all this for a while, I came to thinking that for this a simplest form solution might actually be best. One where I import data manually, don't have to worry about auth because it's all local, and is portable to many other potential personal-data-storage-and-viewing-type applications.</p><br />
    <p >The GitHub repository can be found <a  href="https://github.com/Ulthran/ctbus_finance" target="_blank">here</a>.</p>
    <p >For starters, the two high level data models I created were CreditCard and Account. The distinction here is that an Account holds Holdings, with each Holding being some asset with a ticker symbol (including things like cash or crypto) and a CreditCard is just associated with a balance and a rewards balance. Both CreditCards and Accounts are snapshotted each month with AccountHoldings and CreditCardHoldings, recording the current date, the current quantity, and the current value. All of this is implemented in SQLAlchemy for compatibility with whatever backend we choose.</p>
    class Account(Base):
    __tablename__ = "accounts"
    name = Column(
    String, nullable=False, primary_key=True
    )  # e.g., "My Brokerage Account"
    type = Column(String, nullable=False)  # e.g., brokerage, roth_ira, 403b
    institution = Column(String, nullable=True)  # e.g., Vanguard, Fidelity, Coinbase
    holdings = relationship("AccountHolding", back_populates="account")
    class Holding(Base):
    __tablename__ = "holdings"
    symbol = Column(String, nullable=False, primary_key=True)  # e.g., AAPL, BTC
    name = Column(String, nullable=True)
    asset_type = Column(String, nullable=False)  # e.g., Stock, ETF, Crypto, Cash
    account_holdings = relationship("AccountHolding", back_populates="holding")
    class AccountHolding(Base):
    __tablename__ = "account_holdings"
    __table_args__ = (
    UniqueConstraint(
    "account_id",
    "holding_id",
    "date",
    "purchase_date",
    name="uix_account_holding_date",
    ),
    )
    account_id = Column(
    String, ForeignKey("accounts.name"), primary_key=True, nullable=False
    )
    holding_id = Column(
    String, ForeignKey("holdings.symbol"), primary_key=True, nullable=False
    )
    date = Column(Date, primary_key=True, nullable=False)
    purchase_date = Column(Date, primary_key=True, nullable=True)
    quantity = Column(Float, nullable=False)  # Number of shares/units
    price = Column(Float, nullable=False)  # Price per share/unit
    purchase_price = Column(
    Float, nullable=True
    )  # Price at which the asset was purchased
    # Optional fields
    percentage_cash = Column(Float, nullable=True)  # Percentage of cash in the holding
    percentage_bond = Column(Float, nullable=True)  # Percentage of bond in the holding
    percentage_large_cap = Column(
    Float, nullable=True
    )  # Percentage of large cap stock in the holding
    percentage_mid_cap = Column(
    Float, nullable=True
    )  # Percentage of mid cap stock in the holding
    percentage_small_cap = Column(
    Float, nullable=True
    )  # Percentage of small cap stock in the holding
    percentage_international = Column(
    Float, nullable=True
    )  # Percentage of international stock in the holding
    percentage_other = Column(
    Float, nullable=True
    )  # Percentage of other assets in the holding
    notes = Column(String, nullable=True)  # Notes about the holding
    account = relationship("Account", back_populates="holdings")
    holding = relationship("Holding", back_populates="account_holdings")
    @property
    def total_value(self):
    return self.quantity * self.price
    @property
    def gain_loss(self):
    if self.purchase_price:
    return (self.price - self.purchase_price) * self.quantity
    return None
    class CreditCard(Base):
    __tablename__ = "credit_cards"
    name = Column(String, nullable=False, primary_key=True)  # e.g., "Chase Sapphire"
    institution = Column(String, nullable=True)  # e.g., Chase, American Express
    card_type = Column(String, nullable=False)  # e.g., Visa, Mastercard
    holdings = relationship("CreditCardHolding", back_populates="credit_card")
    class CreditCardHolding(Base):
    __tablename__ = "credit_card_holdings"
    credit_card_id = Column(
    String, ForeignKey("credit_cards.name"), primary_key=True, nullable=False
    )
    date = Column(Date, primary_key=True, nullable=False)
    balance = Column(Float, nullable=False)  # Current balance
    rewards = Column(Float, nullable=True)  # Current rewards balance
    credit_card = relationship("CreditCard", back_populates="holdings")
    @property
    def total_value(self):
    return (self.rewards if self.rewards else 0) - self.balance
    <p >Now that we have these data models, creating ingest and storage functions is a piece of cake. We can use pandas to read CSVs into DataFrames and then the built in <i>to_sql()</i> to load those DataFrames to tables. Behind the scenes, there's a bit more going on to setup a database connection, create the database, and process the CSVs to add things like the current date. You can check out how that works in the GitHub.</p>
    <p >One of the keys to the simplicity of the whole project is SQLite, a widely used, lightweight database solution that lives directly on the filesystem. You can specify the connection to such a database with the URI <i>sqlite:////path/to/db.sqlite</i> and then interact with it as a file and as a database (a sort of file/database superposition).</p>
    <p >Now we have a database full of data and a set of models which provide us clean ways of querying it. It's time to start looking at our data. The first thing I wanted was a function that would provide a list of accounts and their values. We can make use of our SQLAlchemy models to query the database for all AccountHoldings in the month/year of interest and then sum their values per Account.</p>
    account_holdings = (
    session.query(AccountHolding)
    .filter(
    extract("year", AccountHolding.date) == datetime.now().year,
    extract("month", AccountHolding.date) == datetime.now().month,
    )
    .all()
    )
    accounts = [
    (
    a.name,
    a.type,
    a.institution,
    round(
    sum(
    [
    ah.total_value
    for ah in account_holdings
    if ah.account_id == a.name
    ]
    ),
    2,
    ),
    )
    for a in accounts
    ]
    <p >With that we have our per-account valuation! Next we can create an easy net worth function by summing over the results of the accounts and then subtracting the net CreditCard balance. There are a million other things we might investigate down the line, portfolio distribution over different asset classes, net rate of growth, performance of different investments. But that should all be much easier now that we have this simple infrastructure in place to do it. Another addition to this collection might be a quick Flask site, giving us a quick and dirty method for displaying certain stats and graphs that keeps with the theme of running everything locally. I hope this can be useful for you, it certainly is for me! And remember that this framework can be applied to just about any application you want to build that involves data you want to keep track of and have easy access to!</p>
  </v-container>
</template>
