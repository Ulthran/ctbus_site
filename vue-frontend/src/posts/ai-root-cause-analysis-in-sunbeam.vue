<script setup>
import BlogHero from "../components/BlogHero.vue";
import CodeBlock from "../components/CodeBlock.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
const posts = window.posts;
const slug = "ai-root-cause-analysis-in-sunbeam";
const info = posts[slug];

const sunbeamAi = `try:
    client = openai.OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {
                "role": "system",
                "content": "You diagnose errors from Sunbeam pipeline runs. If there are problems, suggest possible causes and solutions. Keep the answer short and sweet. If there are relevant file paths for debugging (like log files), mention them.",
            },
            {
                "role": "user",
                "content": f"Sunbeam ran with the following output:\n{log}\n",
            },
        ],
        max_tokens=1500,
    )
    logger.info(
        "\n\nAI diagnosis:\n"
        resp.choices[0].message.content
        + "\nCheck out the Sunbeam documentation (https://sunbeam.readthedocs.io/en/stable/) and the GitHub issues page (https://github.com/sunbeam-labs/sunbeam/issues) for more information or to open a new issue.\n"
    )
except (
    Exception
) as exc:  # pragma: no cover - network errors are non-deterministic
    logger.error(f"AI analysis failed: {exc}\n")`;
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
    <SectionTitle>AI Beyond Coding</SectionTitle>
    <Paragraph
      >Vibe coding is a powerful tool for software development. But in the field
      of bioinformatics, it's not all about creating software. Even with great
      tooling, you still have to be able to run those tools, troubleshoot the
      results, control metadata and data provenance, and maintain the biological
      context of the work. This brings us to an of-yet-undefined idea of "vibe
      analyzing"; using biological, statistical, and computational knowledge in
      combination with AI to perform higher level bioinformatics
      tasks.</Paragraph
    >

    <SectionTitle>Root Cause Analysis</SectionTitle>
    <Paragraph
      >One of the most straightforward applications of vibe analyzing is
      investigating the root cause of problems in bioinformatic pipelines. The
      idea here is that when something goes wrong, there should be an immediate,
      automated response by an AI that can gather logs, investigate outputs, and
      diagnose the issue with potential remedies. You can see an example of how
      we implemented this in
      <a href="https://github.com/sunbeam-labs/sunbeam">Sunbeam</a>, our
      Snakemake pipeline for metagenomic analysis.</Paragraph
    >

    <SectionTitle>Root Cause Analysis -- Sunbeam</SectionTitle>
    <Paragraph
      >The core of our approach for integrating this feature into Sunbeam is
      using a chat API to automate error triage. Snakemake can often yield huge
      and unwieldy logs with misleading errors scattered around. We started by
      using the OpenAI chat completion API directly with minimal
      complexity:</Paragraph
    >

    <CodeBlock
      :code="sunbeamAi"
      language="python"
      filename="sunbeam/scripts/run.py"
    />

    <Paragraph
      >Next steps from here are making it platform agnostic (using LangChain
      with configurable providers), increasing the useful context we give it
      (include relevant Snakemake and Sunbeam docs with RAG or fine tuning), and
      introducing an agentic approach to dig deeper into outputs and do
      additional research. These will continue to enhance the pipeline's utility
      and availability but for now the simplest solution is a great
      start!</Paragraph
    >
  </v-container>
</template>
