<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "disctracker";
const info = posts[slug];
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :mod_date="info.mod_date"
    :tags="info.tags"
    :img="`/assets/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4 blog-content">
    <Paragraph
      >NOTE: As of writing, this is still very much a work in progress. Don't go
      to these links expecting polished results (or even a living webpage
      sometimes).</Paragraph
    >
    <SectionTitle>Inspiration</SectionTitle>
    <Paragraph
      >I've seen Moneyball (one of the few Michael Lewis books I actually
      haven't read though). I know the power of data to uncover non-obvious and
      non-trivial truths about sports. And with frisbee still being a relatively
      niche and low budget sport, I think there is a big opportunity to
      translate existing tools from more established field sports and apply them
      to frisbee. And I wanted more practice with developing a fullstack
      web/mobile app so this seemed like the perfect project to
      undertake.</Paragraph
    >
    <SectionTitle>Initial Work and Challenges</SectionTitle>
    <Paragraph
      >I started this project by deciding on a split web/mobile architecture
      where the web side of things would do most of the heavy lifting, handling
      the pre- and post-game management, and the app would be purely dedicated
      to real time simplified team management and data input.</Paragraph
    >
    <Paragraph
      >The website I built with Flask and deployed serverlessly with Zappa
      because I had experience with that from this site (and others). The tricky
      part from here, was to integrate with the Cognito authentication that
      comes automatically with the Amplify app. There is already a library for
      managing users on a Flask site via a Cognito User Pool which wasn't too
      difficult to get in place (a few extra things needed setup on the backend
      for it to work properly). However, this doesn't solve the problem of
      getting user-level access to other Amplify resources, such as the GraphQL
      API. For this, I needed to make modifications to the flask-cognito-lib
      plugin that would work with the Cognito ID token (not to be confused with
      the Cognito access token). With this token (and more backend finagling in
      the Identity Pool) the site was able to authenticate users and then access
      relevant backend resources accordingly.</Paragraph
    >
    <Paragraph
      >The app I built with React Native in AWS Amplify because it was one of
      the few options that enabled me to have a web-based interface for the app
      component as well. And as much as I'd like the adhere to the modern idea
      of separating app and mobile codebases, I think there will be opportunity
      in this case for reasonably useful and low risk overlap in usage.
    </Paragraph>
    <SectionTitle>Current Work</SectionTitle>
    <Paragraph
      >My focus now is to provide a POC for the back end of the pipeline,
      essentially the data analytics portion. This means expanding the data
      model to accommodate the current MVP I have in mind as well as thinking
      about as many possible future features as I can and trying to make sure
      the model is extensible to these. I also have some kinks to work out with
      the dev site deployments and with the authentication mechanisms. Once
      that's in place, I'd like to use it (just the back third) for a bit and
      build up a bit of a personal database of game info on which to continue
      refining the data analysis portion.</Paragraph
    >
    <Paragraph
      >Somewhere between finishing the above MVP and acquiring all the data in
      the world, I'll need to get back to focusing on the front two thirds
      again, first expanding the data model to accommodate the types of game and
      tournament planning I want to enable for teams and then actually building
      out to provide the critical part of the UX. Certainly a long way to go but
      I'll keep chipping away at it and hopefully piece by piece build something
      people (including myself) will want to use.</Paragraph
    >
    <SectionTitle>Crazy Aspirations</SectionTitle>
    <Paragraph
      >One of my pipe dreams when starting this project was to create a platform
      where a user could speak directly at their phone/tablet over the course of
      a game and it would parse out relevant "game events" from the dialogue and
      timestamp them. Despite calling it a pipe dream, I do think that this
      feature could follow pretty readily for a well built base product. All it
      would take is access to a voice-to-text module (either built in or
      accessed through an API) and an LLM with some basic training to recognize
      "game events". This comes from the number one issue I've heard from users
      of existing apps for this type of thing: "it's happening too fast and I
      don't want to look at my phone that much." If instead they could just be
      narrating the game, that could make it dramatically easier to follow and
      record the action in a structured format. If any video of the game is also
      timestamped, it will enable me to sync up any kind of video/analysis
      pairing features.</Paragraph
    >
    <Paragraph
      >Linking with other services, like Ultiworld for film and relevant
      articles, USAU for rosters and tournament info, etc. It would take a
      significant user base and a lot of talking but I am building this with the
      mindset that it could (keyword, could) be a one stop shop for all things
      ultimate. I feel like, along with being ambitious, this makes sure that as
      many doors as possible are open for development down the line.</Paragraph
    >
  </v-container>
</template>
