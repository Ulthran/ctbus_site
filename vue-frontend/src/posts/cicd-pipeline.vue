<script setup>
import BlogHero from '../components/BlogHero.vue'
import Paragraph from '../components/Paragraph.vue'
import SectionTitle from '../components/SectionTitle.vue'
import CodeBlock from '../components/CodeBlock.vue'
const posts = window.posts
const slug = 'cicd-pipeline'
const info = posts[slug]
const testsYaml = `name: Tests
on:
  pull_request:
    branches: [main, master]
  push:
    branches: [main, master]
jobs:
  run-tests:
    name: Test Codebase
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install -r dev-requirements.txt
      - name: Run Tests
        run: |
          pytest tests/`

const unitTestPy = `from app.data_utils import get_chess_stats
def test_get_chess_stats():
    # Chess.com's "unofficial" API, meaning they recognize people use it as is
    # but don't provide guarantees that it will stay the same.
    assert not any([v == "ERR" for k, v in get_chess_stats().items()])`

const linterYaml = `name: Super-Linter
on:
  pull_request:
    branches: [main, master]
jobs:
  super-linter:
    name: Lint Codebase
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Run Super-Linter
        uses: github/super-linter@v4
        env:
          VALIDATE_ALL_CODEBASE: true
          GITHUB_TOKEN: \${{ secrets.GITHUB_TOKEN }}
          VALIDATE_PYTHON_BLACK: true
          VALIDATE_JAVASCRIPT_ES: true
          FILTER_REGEX_INCLUDE: app/|tests/`

const buildYaml = `...
build-artifact:
  needs: test
  runs-on: ubuntu-latest
  steps:
    - name: Checkout Code
      uses: actions/checkout@v4
    - name: Install Dependencies to venv
      run: |
        python -m venv env
        source env/bin/activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Build Artifact
      run: |
        source env/bin/activate
        zappa package dev -o ctbus_site.zip
    - name: Upload Artifact
      uses: actions/upload-artifact@v3
      with:
        name: ctbus_site
        path: ./ctbus_site.zip
        retention-days: 1
  ...`

const policyJson = `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "lambda:CreateFunction",
        "s3:ListAccessPointsForObjectLambda",
        "s3:GetAccessPoint",
        "lambda:ListVersionsByFunction",
        "logs:DescribeLogStreams",
        "events:PutRule",
        "route53:GetHostedZone",
        "s3:PutStorageLensConfiguration",
        "cloudformation:DescribeStackResource",
        "lambda:GetFunctionConfiguration",
        "iam:PutRolePolicy",
        "s3:ListStorageLensGroups",
        "apigateway:DELETE",
        "events:ListRuleNamesByTarget",
        "apigateway:PATCH",
        "events:ListRules",
        "cloudformation:UpdateStack",
        "events:RemoveTargets",
        "lambda:DeleteFunction",
        "logs:FilterLogEvents",
        "apigateway:GET",
        "events:ListTargetsByRule",
        "cloudformation:ListStackResources",
        "iam:GetRole",
        "events:DescribeRule",
        "s3:PutAccountPublicAccessBlock",
        "apigateway:PUT",
        "s3:ListAccessPoints",
        "lambda:GetFunction",
        "s3:CreateStorageLensGroup",
        "s3:ListJobs",
        "route53:ListHostedZones",
        "route53:ChangeResourceRecordSets",
        "s3:ListMultiRegionAccessPoints",
        "cloudformation:DescribeStacks",
        "s3:ListStorageLensConfigurations",
        "events:DeleteRule",
        "events:PutTargets",
        "lambda:UpdateFunctionCode",
        "s3:GetAccountPublicAccessBlock",
        "lambda:AddPermission",
        "s3:ListAllMyBuckets",
        "cloudformation:CreateStack",
        "cloudformation:DeleteStack",
        "s3:PutAccessPointPublicAccessBlock",
        "lambda:*",
        "apigateway:POST",
        "s3:CreateJob"
      ],
      "Resource": "*"
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": [
        "iam:PassRole",
        "s3:CreateBucket"
      ],
      "Resource": [
        "arn:aws:s3:::zappa-*",
        "arn:aws:iam::832242454463:role/*-ZappaLambdaExecutionRole"
      ]
    },
    {
      "Sid": "VisualEditor2",
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::zappa-*"
    }
  ]
}`

const deployYaml = `...
dev-deploy:
  needs: build-artifact
  runs-on: ubuntu-latest
  # These permissions are needed to interact with GitHub's OIDC Token endpoint
  permissions:
    id-token: write
    contents: read
  steps:
    - name: Checkout Code
      uses: actions/checkout@v4
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Download Zip
      uses: actions/download-artifact@v3
      with:
        name: ctbus_site
    - name: Configure AWS Credentials
      uses: aws-actions/configure-aws-credentials@v4
      with:
        role-to-assume: arn:aws:iam::832242454463:role/ZappaUserRole
        aws-region: us-east-1
    - name: Setup AWS Profile
      run: |
        aws configure set region us-east-1 --profile default
        aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID --profile default
        aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY --profile default
        aws configure set aws_session_token $AWS_SESSION_TOKEN --profile default
    - name: Deploy to Dev
      run: |
        zappa update dev --zip ctbus_site.zip --json
    - name: Dump Logs
      if: always()
      run: |
        sleep 30
        zappa tail dev --json --since 10m --disable-keep-open
  ...`

const conftestPy = `import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@pytest.fixture
def arg(request):
    return request.getfixturevalue(request.param)

@pytest.fixture()
def setup_chrome():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
    ]
    for option in options_arr:
        options.add_argument(option)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.close()

@pytest.fixture()
def setup_chrome_mobile():
    options = ChromeOptions()
    options_arr = [
        "--headless",
        "--disable-gpu",
        "--window-size=1080,1920",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--user-agent=Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Mobile Safari/537.36",
    ]
    for option in options_arr:
        options.add_argument(option)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.close()`

const testTitlePy = `import pytest
from . import DEV_URL
@pytest.mark.parametrize(
    "arg",
    [
        "setup_chrome",
        "setup_chrome_mobile",
        "setup_chromium",
        "setup_edge",
        "setup_firefox",
    ],
    indirect=True,
)
def test_title(arg):
    driver = arg
    driver.get(DEV_URL)
    assert driver.title == "Charlie Bushman"`

const pageObjPy = `import pytest
from . import DEV_URL
from selenium import webdriver
from selenium.webdriver.common.by import By

class Page:
    def __init__(self, driver: webdriver, url: str):
        self.driver = driver
        driver.get(url)

class Comps(Page):
    def __init__(self, driver: webdriver, url: str):
        super().__init__(driver, f"{url}/projects/comps")
        self.hide_graphs_button = self.driver.find_element(
            By.CLASS_NAME, "interest-button"
        )
        self.lorenz_plots = self.driver.find_element(By.ID, "LorenzPlots")

@pytest.mark.parametrize(
    "arg",
    [
        "setup_chrome",
        "setup_chrome_mobile",
        "setup_chromium",
        "setup_edge",
        "setup_firefox",
    ],
    indirect=True,
)
def test_comps(arg):
    driver = arg
    driver.get(DEV_URL)
    comps = Comps(driver, DEV_URL)
    comps.hide_graphs_button.click()
    assert not comps.lorenz_plots.is_displayed()
    comps.hide_graphs_button.click()
    assert comps.lorenz_plots.is_displayed()`

const accessYaml = `web-accessibility-eval:
  needs: dev-deploy
  runs-on: ubuntu-latest
  steps:
    - name: Web Accessibility Eval
      uses: a11ywatch/github-action@v2.1.9
      with:
        WEBSITE_URL: https://12345abcde.execute-api.us-east-1.amazonaws.com/dev/
        SITE_WIDE: true
        SUBDOMAINS: false
        TLD: false
        SITEMAP: true
        FAIL_ERRORS_COUNT: 15
        LIST: true
        FIX: false
        UPGRADE: false
        UPLOAD: true
      env:
        DEFAULT_RUNNERS: htmlcs,axe
        PAGEMIND_IGNORE_WARNINGS: true
        AI_DISABLED: false`

const zapYaml = `zap-deployment:
  needs: dev-deploy
  runs-on: ubuntu-latest
  steps:
    - name: ZAP Scan
      uses: zaproxy/action-baseline@v0.10.0
      with:
        target: DEV_URL`
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
      <Paragraph>Deploying a zappa site takes time. Not that much, a couple minutes, but it means that it's a pain to do regularly which means that I didn't do it regularly. Instead I developed and tested with a local version and then would push straight to production once that was where I wanted it. And that approach worked, but it had some downsides, such as having to manually deploy changes (even just once in a while) and not catching deployment issues early (like installing huge dependencies and having lambda reject the package for being too big). These are the kind of issues that scale with complexity so I figured I'd get a jumpstart and automate as much as I could now, get the infrastructure in place to go above and beyond the project's CI/CD needs. The end goal is a pipeline like this: version control -> tests/static analysis -> build & push artifact -> dev deployment -> test dev deployment -> prod deployment (on PR merge)</Paragraph>
      <SectionTitle>Starting with Simple CI</SectionTitle>
      <Paragraph>As a starting point, I need to implement some basic CI workflows, which I'm already familiar with from developing scientific software packages. I use GitHub Actions (GHA) for everything cause that's what I'm used to. Adding a unit testing workflow with PyTest is relatively straightforward:</Paragraph>
    <CodeBlock :code="testsYaml" language="yaml" filename=".github/workflows/tests.yml" />
      <Paragraph>With that in place, it's time to develop some unit tests for the site. And lucky for us there's very little to actually unit test. At this point there's really just the main app file, which contains routes and not much more, and a <code>data_utils.py</code> that has one function for retrieving Chess.com stats. Even though it integrates with a 3rd party and so shouldn't technically be included in unit testing, we're gonna call it a unit test anyways.</Paragraph>
    <CodeBlock :code="unitTestPy" language="python" filename="tests/unit/test_data_utils.py" />
      <Paragraph>Upon committing these two files, the tests workflow runs and succeeds! Now I can develop with the confidence that my makeshift Chess.com API won't break (either with my changes or theirs, again, not really a proper unit test). I also want a linting workflow to enforce formatting for my codebase. I'm going to use Super Linter because it's a super easy way to manage linting many different languages through GitHub Actions.</Paragraph>
    <CodeBlock :code="linterYaml" language="yaml" filename=".github/workflows/linter.yml" />
      <Paragraph>With that committed as well, I can now develop with confidence that my changes won't introduce poorly formatted code or break existing functionality! But there's one more thing I want to add before moving on and that's static analysis. Especially since I have started using AI dev tools like GitHub Copilot and ChatGPT for code generation, it's important to have constant static analysis checks to catch dangerous patterns I don't catch. Codacy links directly with GitHub to do its work without any configuration files necessary (see <a href="https://docs.codacy.com/v3.4/getting-started/getting-started-with-codacy/" target="_blank" >Codacy Docs</a>).</Paragraph>
      <SectionTitle>Turning Focus to CD</SectionTitle>
      <Paragraph>In the interim between the last step and now, I took a course called DevOps Foundations on LinkedIn Learning, leading me to think I should expand my CI to include CD. This presents a few challenges I've never faced before: 1) interacting with GitHub's artifact repository, 2) authorizing a GitHub Action to deploy changes to AWS, and 3) performing tests and security audits on the deployed site. Turns out the first one, interacting with artifacts, is super easy! They already have prebuilt actions for doing everything you need to do (push and pull) and zappa has utilities for building and deploying zips (instead of doing it all in one command).</Paragraph>
    <CodeBlock :code="buildYaml" language="yaml" filename=".github/workflows/CICD.yml" />
      <SectionTitle>AWS and GitHub Actions</SectionTitle>
      <Paragraph>Authorizing a GHA runner to interact with AWS was not quite as straightforward, despite being relatively well documented. As with most things involving AWS IAM, there are a lot of options that introduce a lot of complexity. Most of the work on GitHub's side is covered by the <a href="https://github.com/aws-actions/configure-aws-credentials" target="_blank" >Configure AWS Credentials</a> action. My first thought was that I'd be able to just plop credentials for an AWS profile in as GHA environment variables but the recommendation is not to do that, instead preferring OpenID Connect. Through this method, an Idendity Provider (IdP) is setup in AWS IAM and then a Role is created that trusts the IdP. That Role can then be used with GHA. Setting up the IdP in AWS IAM and connecting the Role are covered in <a href="https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services#adding-the-identity-provider-to-aws" target="_blank" >Configuring OpenID Connect in Amazon Web Services</a>. The only setup left to do in AWS then is to create a Policy for the Role that will give zappa the necessary permissions to do its work. I couldn't find any examples of such a Policy so I've included the one I pieced together here.</Paragraph>
    <CodeBlock :code="policyJson" language="json" filename="policy.json" />
      <Paragraph>To use this in your own project, you'll have to change the User identifier in the Resource spec <code>"arn:aws:iam::832242454463:role/*-ZappaLambdaExecutionRole"</code>. Once all that is working, the rest is pretty easy, just have to configure the AWS CLI and run the right zappa commands.</Paragraph>
    <CodeBlock :code="deployYaml" language="yaml" filename=".github/workflows/CICD.yml" />
      <SectionTitle>Testing an Active Website</SectionTitle>
      <Paragraph>This is a part I have no prior experience with. I need tools which I can run in GHAs that will perform a healthy subset of the possible classes of tests for web apps. This article on <a href="https://www.browserstack.com/guide/how-to-perform-website-qa-testing" target="_blank" >How to Perform Website QA Testing</a> is pretty helpful in creating a mental framework for this, but probably goes more in depth than I need. My thinking is that the major ones to focus on will be functionality testing, cross-browser/cross-device testing, accessibility testing, and penetration testing.</Paragraph>
      <Paragraph>The first two, functionality and cross-browser/cross-device testing, can both be handled by Selenium, which is nice enough to have a solid Python interface for us to use (as well as every other language you could want). The core idea of selenium is that you can set up a WebDriver object that mimics the behavior of whichever browser you want and then use that object to perform actions on the website as the user would and check that the results are as expected. This allows you to abstract away problems with display, browser, os, etc. and just focus on testing critical user paths. So the first step is to setup a WebDriver in PyTest.</Paragraph>
    <CodeBlock :code="conftestPy" language="python" filename="tests/e2e/conftest.py" />
      <Paragraph>OK I went overboard and setup two WebDrivers: one for testing Chrome and one for testing Chrome on a mobile device. I also created this weird <code>arg</code> function so that I can use PyTest fixture parameterization to run the same tests on each of my WebDriver fixtures.</Paragraph>
    <CodeBlock :code="testTitlePy" language="python" filename="tests/e2e/test_web.py" />
      <Paragraph>Obviously this test is little more than a PoC for running tests on multiple web drivers though. In order to actually start testing useful features, I read the Selenium docs and learned about their PageObject testing structure. Under this paradigm, each page of the site is abstracted to a PageObject that models objects on the page within the test code. These PageObjects can then be used to perform higher-level feature testing without worrying about implementation changes in the actual page. Here's an example of that with a button for hiding graphs (not the most critical, but nice to know it will work).</Paragraph>
    <CodeBlock :code="pageObjPy" language="python" filename="tests/e2e/test_web.py" />
      <Paragraph>This idea can be extended to any other user flows that need testing (but I don't really have any on the site right now, mostly just readable content). So it's time to move on to the next type of website testing: accessibility testing. Fortunately, there is a prebuilt <a href="https://github.com/a11ywatch/github-actions" target="_blank" >GHA from A11ywatch</a> that has all the features one could ask for and more that one didn't think to ask for. Including it in the pipeline is not quite a piece of cake though, and that's because of the crazy API Gateway URL of the dev site deployment. (This hasn't been resolved yet but I'll try to update this when it is. For now, here's example code for running their action just on the home page of my site.)</Paragraph>
    <CodeBlock :code="accessYaml" language="yaml" filename=".github/workflows/CICD.yml" />
      <Paragraph>The final testing variant that needs to be included in the pipeline is penetration testing. Although, admittedly, I'm not super worried about the security of a website that neither stores nor accepts user data (for now) and is open source. Regardless, a super, prebuilt GHA comes to my rescue again in the form of the <a href="https://github.com/zaproxy/action-baseline" target="_blank" >ZAP Scan Action</a>. Super easy to implement and provides a very helpful report at the end with all its findings.</Paragraph>
    <CodeBlock :code="zapYaml" language="yaml" filename=".github/workflows/CICD.yml" />
      <SectionTitle>Conclusions</SectionTitle>
      <Paragraph>I wasn't convinced this would actually be useful at the start of this project. It was more of a learning project and something that might come in handy if this site ever scales up significantly. But I was absolutely wrong! Just in the process of building the PR to add this workflow I caught so many things that I normally wouldn't until later down the line or at all. I could see within minutes whether or not site configuration changes had messed up the actual deployment. I made low contrast elements and images without alt text more accessible. I added Content Security Policy headers to prevent common attacks. The positive impact that this pipeline has had on my web app practices and should continue to have on this site when I forget these practices in the future or encounter new terrain is enormous.</Paragraph>
    <img src="CDN_URL/images/ctbus_site_cd_workflow_success.png" alt="CI/CD Workflow Success" >
      <Paragraph>And it's free. As long as the project is open source on GitHub, I have as much GHA runner usage as I can handle. If you have a web app deployed through zappa, there's almost no downside to implementing a similar CI/CD pipeline to improve the quality, security, and accessibility of your app.</Paragraph>
  </v-container>
</template>
