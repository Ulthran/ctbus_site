<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "flask-sessions";
const info = posts[slug];
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`${window.assetsBase}/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <Paragraph
      >The issue of storing session data on this site came up when I started
      trying to build a Spotify stats visualizer. The Spotify Web API requires
      an access token which is retrieved with a combination of the app's API key
      and the user's login information. The access token then has to be stored
      somehow so that the user doesn't have to login again every time the app
      makes a request. In the case of a web app, it is stored as session data.
      And as it happens, there are a lot of ways to store session data for a
      website.</Paragraph
    >
    <SectionTitle>What is Session Data</SectionTitle>
    <Paragraph
      >Session data is information that is associated with a particular user of
      a website and that persists for some amount of time. It can be stored
      locally on a user's computer, locally on the server running the website,
      or in a remote database. How it is persisted can also vary to dependent on
      a timeout, a user action, an administrator action, etc. There are not so
      minute minutiae I'm skimming here like the difference between session and
      cookies and more I'm probably not aware of but for this case I was just
      looking for the simplest way to persist information for a user on my
      site.</Paragraph
    >
    <SectionTitle>First Try: Flask-Session with Filesystem</SectionTitle>
    <Paragraph
      >The first way I tried to store session data was with Flask-Session and
      the filesystem. This was the simplest way to store session data and it
      worked fine in test. The issues started when I deployed these changes to
      the dev site. It could create the session data just fine but every time a
      new page loaded it would wipe all the existing data. The reason for this
      is pretty obvious in hindsight (or to anyone who took note of the warnings
      in the Flask Session docs). This site is deployed serverlessly on AWS
      Lambda which means that every time a new page loads, it is actually a new
      server being spun up to serve that page. If we store session data on the
      server's filesystem, every time a new page loads, we get a new filesystem
      and the data is apparently gone. So we need a method that doesn't rely on
      persisting information on the server.</Paragraph
    >
    <SectionTitle
      >Second Try: Flask-Session with Memcache (AWS ElastiCache)</SectionTitle
    >
    <Paragraph
      >The second and most expensive way I tried to store session data was with
      Flask-Session and Memcache. This was a bit more complicated than the
      filesystem method because it required a new piece of infrastructure. I set
      up an AWS ElastiCache instance and configured Flask-Session to use it.
      There were two problems I came upon here. The first was the networking of
      my AWS resources. ElastiCache is designed to be internal to AWS, meaning
      it is mostly meant to be accessed by AWS resources. We are trying to
      access it from a Lambda function, so in luck there, but this meant that we
      had to modify our deployment to be within the same Virtual Private Cloud
      (VPC) as the ElastiCache deployment. On top of this, a Network Address
      Translation (NAT) Gateway was also needed to make this site still be
      accessible from outside the VPC. And it turns out that both of these new
      components (ElastiCache database and NAT Gateway) are expensive. They're
      not outrageous if you already have monthly tech infrastructure costs, but
      if you're trying to keep your personal site mostly in free tier, they're
      insane. So I abandoned this plan too and was about ready to give up on the
      Spotify stats app.</Paragraph
    >
    <SectionTitle
      >Third Try: Flask's Built-In <i>session</i> Object</SectionTitle
    >
    <Paragraph
      >Then I realized I had made a significant oversight in my initial overview
      of the options available to me. Flask (without Flask Session) has a built
      in session object. And that session stores data locally to the user's
      computer. I tried this way out and it worked immediately. Even better, it
      incurs no added cost and doesn't add any dependencies to the site (keeping
      bundle size down). So this is what I went with. And it still gives the
      ability to have a page where you (the user) can
      <a href="/session" target="_blank">view and delete session data</a> from
      this site.</Paragraph
    >
    <Paragraph
      >This was my first foray into using session data on a website. If you have
      experience with it and want to provide feedback/critique or if you have
      none and want to know more about my setup, please send me an email.
      :)</Paragraph
    >
  </v-container>
</template>
