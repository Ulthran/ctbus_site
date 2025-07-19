<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "multi-dev-deployment";
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
    <SectionTitle>Intro</SectionTitle>
    <i
      >Some background on the
      <a href="">original CI/CD pipeline I created for this site</a> and on the
      <a href="">Ultimate Disctracker (UDT)</a> project (which I copied a lot of
      the CI/CD for) linked here.</i
    >
    <Paragraph
      >As a tl;dr for those who don't want to read those other articles, for
      this site and another that I developed with Flask, I created a CI/CD
      pipeline that will deploy test changes to a dev site for further testing
      (automated and manual) before deploying to production. The issue with my
      setup was that I only had one dev site, so if I made changes on one branch
      then made changes on another, the later changes would overwrite the
      earlier ones. The obvious solution is to deploy each development branch to
      its own dev site.</Paragraph
    >
    <SectionTitle
      >First Attempt: Deploying to
      <i>dev.charliebushman.com/feature-branch-name</i></SectionTitle
    >
    <Paragraph
      >My first thought was to have a single dev subdomain which would then map
      each dev deployment to a different base path. I created a CloudFormation
      script to create and delete the necessary resources that included
      deploying the site to API Gateway and creating a BasePathMapping under the
      dev domain to this new site. Unfortunately, the result of doing this was a
      bunch of confused deployments that were all trying to source files from
      the root path still (instead of their new base paths). I tried adapting
      the site into a blueprint to account for this behavior but I couldn't get
      it to work this way (if anyone comes up with a working version of this
      solution let me know).</Paragraph
    >
    <SectionTitle>New Strategy: Deploying to dev subdomains</SectionTitle>
    <Paragraph
      >Once I realized the limitations on that plan, I came back to an earlier
      solution I had considered. Deploying each dev site to its own subdomain. I
      had thought that this wasn't feasible for the resources that would have to
      be set up around each subdomain, but with a little research I found that
      most of those aren't actually necessary. I modified the CloudFormation
      script to deploy the site to API Gateway, create a new Custom Domain (in
      API Gateway), add the root BasePathMapping to my new function, and then
      add a record to the Route53 Hosted Zone to alias the new subdomain. And
      what's more, all this can be done with a single certificate that uses
      <i>*.charliebushman.com</i> as its domain!</Paragraph
    >
    <SectionTitle>Conclusion</SectionTitle>
    <Paragraph
      >The end result for me is just removing the occasional dev headache.
      However, if there were a team of developers working on a site, this would
      be an absolute essential. Keeping dev deployments from overlapping
      requires more work but is well worth the siloed testing environments you
      end up with. And with the CloudFormation script, it's easy to automate the
      deletion of all those resources when the feature branch is
      deleted.</Paragraph
    >
  </v-container>
</template>
