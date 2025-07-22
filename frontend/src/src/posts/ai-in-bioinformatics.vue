<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
const posts = window.posts;
const slug = "ai-in-bioinformatics";
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
    <SectionTitle>The State of Bioinformatics</SectionTitle>
    <Paragraph
      >Bioinformatics is the enourmous and rapidly growing field of applying
      computation and statistics to biological problems in the hopes of
      elucidating underlying processes. Successes big and small come out from
      bioinformatics research every day from improved understanding of cancers
      to improved hygiene in hospitals. It is arguably the science with the
      fastest average time from exploratory research to life altering effects on
      the population. One of the major trends in bioinformatic research, upon
      realizing the importance of a new field such as the gut microbiome, is to
      start a long period of data gathering and synthesis. This means taking
      hundreds and hundreds of thousands of samples from healthy and sick people
      and running them through massive data pipelines to extract and document
      patterns. Once this has been done long enough, this map of patterns can be
      applied in clinical settings, deriving critical diagnostic information
      from what would otherwise be gibberish.</Paragraph
    >

    <SectionTitle>Often Inexact</SectionTitle>
    <Paragraph
      >The complexity of these underlying systems is almost incomprehensible. To
      use one of the most well known examples -- sequencing the human genome --
      many believed that once the human genome was sequenced we would hold the
      key to everything from how tall someone would grow to what diseases they
      might contract. But the Human Genome Project was completed in 2003,
      sequencing whole human genomes is now common place, and we can hardly
      predict a baby's full grown height any better than in 1990. This is
      because we're in the field of <i>bio</i>informatics not just informatics.
      And that prefix adds whole worlds of complexity behind every supposed
      "bit" of human code.</Paragraph
    >

    <SectionTitle>AI in Bioinformatics</SectionTitle>
    <Paragraph
      >The explosion of AI in 2023 forced many in bioinformatics to ask the
      question, how can we use this? And the obvious holy grail many looked to
      is an AI that can perform the clinical diagnostic job. But that
      dramatically overestimates the capabilities of AI. While I do think it has
      the potential to do this (and has already been implemented as such in more
      thoroughly researched fields) it won't allow us to skip the steps of data
      gathering and analysis that come before. That's not a reason to give up on
      AI in the field though, because it can help with all of these foundational
      parts as well!</Paragraph
    >

    <Paragraph
      >In a series of short articles, I am going to go through what I see as the
      most powerful applications of AI in bioinformatics. This will start with
      concrete examples of tools I use daily to design and debug bioinformatic
      software and provide stepping stones from there to a very speculative look
      at how AI can end up as a diagnostic tool.</Paragraph
    >

    <SectionTitle>Data Governance</SectionTitle>
    <Paragraph
      >Can't forget! Proper data governance is core to any AI solution and this
      is particularly true in a field where human samples are often front and
      center. Maintaining a clear boundary between raw and anonymized data is
      critical to ensure HIPPA compliance. If your institution has an in-house
      AI platform, it will always be easier for data governance purposes to use
      that over third party options. But if you are using a third party AI
      platform, make sure data is both anonymized and doesn't include
      proprietary information.</Paragraph
    >
  </v-container>
</template>
