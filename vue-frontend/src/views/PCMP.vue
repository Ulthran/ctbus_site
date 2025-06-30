<script setup>
import SimplePage from '../components/SimplePage.vue'
const CDN_URL = window.CDN_URL || ''
</script>

<template>
  <SimplePage title="Pcmp">
    <details >
    <summary >What is Metagenomics?</summary>
    <p >If genetics is the study of individual genes and genomics is the study of the collections of genes that make up individual genomes, metagenomics is the study of populations of genomes. Specifically multi-species/genera/families/etc. populations, such as the human gut microbiome which is the main focus of my work.</p>
    </details>
    <details >
    <summary >What exactly do you do?</summary>
    <p >I'm the only designated software engineer in the PCMP; others in the program range from pure wet lab scientists to PhD bioinformaticians. At a high level, my job is to set standards for software across the program and ensure everything meets those standards. In practice, that also means that I am responsible for the brunt of the implementation and refactoring work on published work. In addition to all this, I've come into the role of architecting, creating, and deploying internal services such as preprocessing automation, compute resources, and utility services.</p>
    </details>
    <details >
    <summary >What stack do you use?</summary>
    <p >I work on a lot of different projects so I jump between a bunch of tech stacks. Python is the most common language with R following. For pipelines I typically use Snakemake, a Python workflow DSL, and Prefect, a Python automation framework. Compute is split between in-house HPCs and AWS. Version control is split between Enterprise GitHub and GitHub. CI/CD is largely implemented through GitHub Actions.</p>
    </details>
    <details >
    <summary >How do you use ML/AI?</summary>
    <p >Machine learning and, to a growing degree, generative artificial intelligence are hugely important in bioinformatics. There is a whole host of deep learning tools that are integrated into our pipelines and downstream analyses commonly involve unsupervised classification techniques. I have also begun to integrate self hosted agents and knowledge bases into pipelines but the administrative hurdles to deploying those into practice are significant in a research hospital.</p>
    </details>
    <details >
    <summary >Can I see?</summary>
    <p >Yes! Most of my work is open source and I've listed out projects I've worked on below.</p>
    </details>
    <p >Most of the work I do with the PCMP involves getting sequencing data from one form and transforming it to another. Doing this in a way that is well documented, reproducible, and performant is critical for being able to publish the results of downstream analysis.</p>
    <!-- Project Cards -->
    <p >Some of the cleanest and most straightforward work I do is in helping researchers developing a new statistical method to create a well-packaged software solution to accompany publication. Easy to use and install statistical packages help drive citations for the paper.</p>
    <p >Some methods just aren't worth publishing, whether they're too mundane or too unique to bother. But these methods still need to be reliable and easy to use internally.</p>
    <p >I've built and modified some services for tracking and storing sequencing data as it passes through the PCMP.</p>
    <p >I've developed some tools for improving bioinformatics software development. A lot revolves around the Sunbeam ecosystem for new extensions and testing.</p>
  </SimplePage>
</template>
