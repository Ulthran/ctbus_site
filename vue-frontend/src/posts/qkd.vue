<script setup>
import BlogHero from "../components/BlogHero.vue";
import Paragraph from "../components/Paragraph.vue";
import SectionTitle from "../components/SectionTitle.vue";
import CodeBlock from "../components/CodeBlock.vue";
const posts = window.posts;
const slug = "qkd";
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
      >Towards the end of Junior year quantum mechanics we were given an
      assignment along the lines of go find something cool (quantum mechanics
      related) and research it and write a short paper on your findings. I
      picked quantum key distribution (QKD) as my subject because it sounds
      cool. Turns out, it also is cool. There's a fair amount of groundwork to
      do to convince others of that though; I'll do my best here, then you can
      read the paper.</Paragraph
    >
    <SectionTitle>What is This and Why Do We Care?</SectionTitle>
    <Paragraph
      >One of the oldest and most widely used cryptographic algorithms is RSA,
      which uses a public and private key to encrypt and decrypt messages and
      which relies on the computational complexity of factoring prime numbers
      for its security. If I want to send you a message using RSA, the steps are
      fairly straightforward. First, you take two big prime numbers and you
      multiply them together. The product is your public key and the two
      starting numbers are your private key (oversimplification). You make your
      public key public so that I can find it (as can anyone else who might be
      eavesdropping). Second, I encrypt the super secret file I want to send you
      with this big number using the RSA algorithm. Then I can send you the
      encrypted file without worrying about anyone eavesdropping because even if
      they see what I send, it's just jibberish without the two prime numbers
      you kept to yourself. You, with the two prime numbers, can use RSA sort of
      in reverse to decrypt the super secret file.</Paragraph
    >
    <Paragraph
      >RSA and similar algorithms have been the standard in electronic
      encryption since before the internet and have been pretty much unbreakable
      due to the enormous complexity of factoring a very, very, very large
      number (even with only two factors). But then, in 1998, the first quantum
      computer became functional (quantum computers are just barely older than I
      am). And although it would take a few decades to even enter the realm of
      plausibility, a technology that could (one day) break RSA had just been
      proven to work. But it also came packaged with a solution for the problem
      it caused, quantum key distribution.</Paragraph
    >
    <Paragraph
      >QKD is a totally different encryption scheme from RSA and cannot be
      broken even with a quantum computer (in theory). This is because it relies
      on quantum information which will show signs of tampering as soon as
      anyone reads it. There are different QKD algorithms but the basic
      principle underlying them all is to use quantum information exchanged over
      potentially untrustworthy networks to get two parties to share some number
      of bits of information which can then be used to encrypt and decrypt
      messages.</Paragraph
    >
    <Paragraph
      >Before you go further and get too invested in QKD, a couple disclaimers.
      First, QKD requires a lot of infrastructure that only sort of exists. The
      most commonly proposed is a network of fiber optic cables for transmitting
      photonic qubits. That's a lot of effort and will likely not be in common
      practice any time terribly soon. Second, the more likely near/mid-term
      solution to quantum computers breaking classical cryptography is
      quantum-resistant classical cryptography. Yes it exists, but the field is
      still very new and NIST has yet to decide on a set of algorithms that will
      be standardized going forward. There's a whole world of crazy math to dive
      into
      <a
        href="https://www.nist.gov/news-events/news/2022/07/nist-announces-first-four-quantum-resistant-cryptographic-algorithms"
        target="_blank"
        >there</a
      >.</Paragraph
    >
    <SectionTitle
      >A Quick Briefing in Information Theory and Quantum Information
      Theory</SectionTitle
    >
    <Paragraph
      >Information theory is a surprisingly recent field that is also
      surprisingly fundamental. The basic idea behind it is that the information
      content of anything can be quantified by determining how many bits it
      would take to represent it. For instance, the number 1000 encodes 10 bits
      of information because in binary it is 1111101000. The number 1 only has 1
      bit of information. But information content is also context dependent. In
      the context of picking a random number, 127 encodes 7 bits of information
      because its binary representation is 1111111. However, 1111111 taken as a
      string, has extremely low entropy -- essentially randomness -- and as such
      has a low information content. You can easily get into some mind bending
      situations if you don't keep track of your context as you calculate
      information content.</Paragraph
    >
    <Paragraph
      >Extending this to quantum information theory, the only thing that changes
      is the unit, the bit, becomes a quantum bit (qubit). Now instead of a bit
      encoding either 1 or 0, it is a superposition of the two, which can be
      represented as a vector of two real (normalized) numbers. So in theory a
      qubit holds infinitely more information than a bit, though in practice our
      ability to measure a qubit's exact state without error is severely lacking
      with current technology. The advantage that this gives quantum computing
      over classical is that it turns all your logic operations into big
      matrices that can chug through NP-hard problems very efficiently (problems
      like cracking RSA).</Paragraph
    >
    <Paragraph
      >There are a couple weird rules with qubits that I feel compelled to cover
      before letting you go off and read my little paper. The first is that
      qubits cannot be copied. We know of no physical way in which someone can
      take a qubit and make an exact copy of it without changing the value of
      the original. The second is that a qubit can only hold information in one
      of many bases and when it is measured in a different basis its information
      content will change. Basically, qubits are very finicky about information
      access in ways that make the universe work as we know it. Now you're
      ready, enjoy!</Paragraph
    >
  </v-container>
</template>
