<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
const posts = window.posts;
const slug = "vibe-coding-in-bioinformatics";
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
    <SectionTitle>AI as a Developer Tool</SectionTitle>
    <Paragraph
      >The most immediate place that AI can (and does) make real impacts on the
      field of bioinformatics is as a coding assistant. It has already arguably
      reached the level of a junior developer and that means it can already
      surpass a number of scientists/bioinformaticians in pure software design
      and implementation. But it is not nearly as good at capturing
      scientifically inspired code requirements or edge cases as the researcher.
      So we have this situation where there is a pretty decent but naive coder
      and a scientist who knows (roughly) what they want. This is not a new
      paradigm; it requires scientists to take on the role of project manager
      and allow the AI to be the developer. This is a pattern that will continue
      through this series as we find ways to leverage AI to cover more and more
      layers of abstraction in the research process.
    </Paragraph>

    <SectionTitle>Code Completion</SectionTitle>
    <Paragraph
      >In its simplest form, AI can be used to provide near real time
      autocomplete suggestions for code based on knowledge of the language,
      libraries, and even the context of other files in the project. This is a
      great way to speed up development and reduce the cognitive load of
      remembering syntax and library functions. It can be included in IDEs or
      notebooks for direct coding tasks. It can also be included in
      browser-based applications like helping users design SQL queries to submit
      for a database (like we do
      <a href="https://github.com/PennChopMicrobiomeProgram/marc_web">here</a>).
      There is almost no barrier to entry here for the users and setup is often
      straightforward as well. There's almost no reason not to use smart
      completion wherever you code.</Paragraph
    >

    <SectionTitle>Code Chat</SectionTitle>
    <Paragraph
      >The next step up from code completion is a chat-based interface with your
      code. By creating a natural language interface with code, it lowers the
      barrier to entry for performing more advanced bioinformatic analysis or
      building automations. The efficacy of code chat can vary widely by
      foundation model, use case, and user experience but it does a lot to
      democratize computational literacy and ability.</Paragraph
    >

    <SectionTitle>Developer Agents</SectionTitle>
    <Paragraph
      >Chatting with your code is good. What's even better is chatting with an
      agent that can chat with your code, search the internet, remember your
      previous talks, and even perform bioinformatic analysis to inform coding
      decisions. The idea of an "AI agent" is essentially treating a single
      instance of an AI chatbot as an individual actor and having it interact
      with others. You can give agents special roles, tools, and knowledge in
      order to perform their job. The end result is an interface similar to code
      chat but with far more capability. You can use third party implementations
      such as OpenAI's Codex, especially for open source development work. For
      sensitive or proprietary development, you may want to explore custom
      implementations using frameworks like Ollama, CrewAI, or
      LangChain.</Paragraph
    >

    <Paragraph
      >I can't overstate how powerful agentic development can be in the right
      contexts. For the purposes of prototyping new ideas, migrating between
      languages or frameworks, and understanding existing code it has easily
      10x'ed the speed of my work and (I believe) improved the overall quality.
      It is most effective iterating fast in low risk environments and you need
      a good sense of the types of tasks it can and can't handle. Like with any
      tool, it requires practice. Try it out wherever you get the
      chance!</Paragraph
    >
  </v-container>
</template>
