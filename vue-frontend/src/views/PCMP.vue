<script setup>
import { ref } from 'vue'
import Hero from '../components/Hero.vue'

const featured = [
  {
    title: 'Sunbeam',
    link: 'https://github.com/sunbeam-labs/sunbeam',
    img: `CDN_URL/images/sunbeam_logo.png`,
    desc: 'A robust and extensible Snakemake pipeline for metagenomic sequencing analysis.',
    did: "One of the program's primary tools for analysis, I have led the open source development of the pipeline since 2022 through multiple major releases. I have also developed and continue to maintain many of the pipeline's extensions.",
  },
  {
    title: 'Condabot',
    link: 'https://github.com/sunbeam-labs/condabot',
    img: `CDN_URL/images/bioconda_logo.png`,
    desc: 'Automates dependency updates for Conda environments across our projects.',
    did: 'This is a DevOps utility I created to keep our Conda environments up-to-date with the latest package versions, ensuring reproducibility and reliability. Conda presents several unique challenges for dependency management, and this tool helps bioinformaticians navigate them.',
  },
  {
    title: 'DEMIC',
    link: 'https://github.com/Ulthran/DEMIC',
    img: `CDN_URL/images/DEMIC_replication_nbg.png`,
    desc: 'Dense statistical package for estimating microbial growth rates from sequencing data.',
    did: 'In my first year with the program I refactored and extended most of the code in this package, including the development of a new preprocessing software (PyCov3) and a Sunbeam extension (sbx_demic). I also wrote the documentation and tutorials for the package.',
  },
  {
    title: 'AutoBfx',
    img: `CDN_URL/images/autobfx_logo.png`,
    desc: 'A modern, terabyte scale automation preprocessing system for sequencing data.',
    did: "I led the development of this Prefect-based workflow system. From ideation with the bioinformaticians and PIs who's time was being sucked into repetitive, error-prone computation, I have built a system that moves projects from the wet lab to exploratory data analysis with no human interaction.",
  },
]

const others = [
  { title: 'AutoBfx', link: '#', desc: 'Prefect based automation for early sequencing analysis.' },
  { title: 'sbx_assembly', link: 'https://github.com/sunbeam-labs/sbx_assembly', desc: 'Extension for contig assembly and annotation.' },
  { title: 'sbx_coassembly', link: 'https://github.com/sunbeam-labs/sbx_coassembly', desc: 'Co-assemble reads from groups of samples.' },
  { title: 'sbx_mapping', link: 'https://github.com/sunbeam-labs/sbx_mapping', desc: 'Map reads to reference genomes with custom filtering.' },
  { title: 'sbx_kraken', link: 'https://github.com/sunbeam-labs/sbx_kraken', desc: 'Taxonomic assignment of reads using Kraken.' },
  { title: 'sbx_demic', link: 'https://github.com/sunbeam-labs/sbx_demic', desc: 'Estimate bacterial growth rates via PTRs.' },
  { title: 'sbx_gene_clusters', link: 'https://github.com/sunbeam-labs/sbx_gene_clusters', desc: 'Align reads to gene clusters of interest.' },
  { title: 'sbx_genome_assembly', link: 'https://github.com/sunbeam-labs/sbx_genome_assembly', desc: 'Pipeline for de novo microbial genome assembly.' },
  { title: 'sbx_virus_id', link: 'https://github.com/sunbeam-labs/sbx_virus_id', desc: 'Identify and annotate viruses from metagenomic samples.' },
  { title: 'sbx_marker_magu', link: 'https://github.com/Ulthran/sbx_marker_magu', desc: 'Detect and quantify phages, bacteria and archaea with Marker-MAGu.' },
  { title: 'sbx_mgv', link: 'https://github.com/Ulthran/sbx_mgv', desc: 'Classify viral sequences using MGV.' },
  { title: 'sbx_seeker', link: 'https://github.com/Ulthran/sbx_seeker', desc: 'Discriminate virus and phage sequences with Seeker.' },
  { title: 'q2-unassigner', link: 'https://github.com/Ulthran/q2-unassigner', desc: 'QIIME2 plugin evaluating closeness of 16S sequences to named species.' },
  { title: 'WFRCWF', link: 'https://github.com/PennChopMicrobiomeProgram/wfrcwf', desc: 'Early work on a simplified pipeline DSL.' },
  { title: 'DEMIC', link: 'https://github.com/Ulthran/demic', desc: 'Dynamic estimator of microbial communities.' },
  { title: 'unassigner', link: 'https://github.com/PennChopMicrobiomeProgram/unassigner', desc: 'Evaluate consistency of 16S sequences with named species.' },
  { title: 'ZIBR', link: 'https://github.com/PennChopMicrobiomeProgram/ZIBR', desc: 'Zero-Inflated Beta Random Effects model for longitudinal data.' },
  { title: 'DAFOT', link: 'https://github.com/lakerwsl/DAFOT', desc: 'Detector of Active Flow On a Tree two-sample test.' },
  { title: 'ShotgunUniFrac', link: 'https://github.com/Ulthran/ShotgunUnifrac', desc: 'Build phylogenetic trees for many genes from NCBI.' },
  { title: 'PyCov3', link: 'https://github.com/Ulthran/pycov3', desc: 'Generate cov3 coverage files used by the DEMIC package.' },
  { title: 'primertrim', link: 'https://github.com/PennChopMicrobiomeProgram/primertrim', desc: 'Trim primer sequences from FASTQ reads.' },
  { title: 'DNAbc', link: 'https://github.com/PennChopMicrobiomeProgram/dnabc', desc: 'Identify DNA barcodes and demultiplex FASTQ data.' },
  { title: 'heyfastq', link: 'https://github.com/kylebittinger/heyfastq', desc: 'Library for reading and mutating FASTQ files.' },
  { title: 'PCMP Metadata Checker', link: 'https://github.com/PennChopMicrobiomeProgram/CHOP_metadata_checker', desc: 'Flask app verifying project metadata meets PCMP standards.' },
  { title: 'PCMP Sample Registry', link: 'https://github.com/PennChopMicrobiomeProgram/SampleRegistry', desc: 'Kubernetes hosted app tracking all sequenced samples.' },
  { title: 'Conda Env Check', link: 'https://github.com/Ulthran/conda_env_check', desc: 'GitHub Action that validates and reports on Conda environments.' },
  { title: 'sbx_test_action', link: 'https://github.com/sunbeam-labs/sbx_test_action', desc: 'GitHub Action to test Sunbeam extensions in CI.' },
]
</script>

<template>
  <Hero title="Developer in Statistical Metagenomics" subtitle="Penn-CHOP Microbiome Program" />

  <v-container class="text-center">
    <v-row>
      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">About the PCMP</h2>
        <p>
          The Penn‑CHOP Microbiome Program is a joint effort between the Perelman
          School of Medicine at the University of Pennsylvania and the Children&#39;s
          Hospital of Philadelphia. The program supports researchers studying the
          microbiome by providing analysis expertise, open-source tools and
          compute infrastructure.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">Human Gut Metagenomics</h2>
        <p>
          The human gut contains trillions of microbes. Instead of culturing each
          one individually, we sequence all DNA from a sample and use computational
          pipelines to piece together who is there and what they&#39;re doing. These
          approaches reveal links between the microbiome and health or disease.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">My Role</h2>
        <p>
          As the program&#39;s software engineer I establish development standards,
          refactor published work and build internal services ranging from
          preprocessing automation to statistical packages. I have led many projects 
          through from creation to production or through major upgrades, often 
          working cross-functionally with researchers and analysts across lab groups.
        </p>
      </v-col>

      <v-col cols="12" md="6" class="text-center">
        <h2 class="text-h6 font-weight-bold mb-2">Tech Stack</h2>
        <p>
          Python and R make up the core of our work with frameworks like Snakemake,
          Prefect, Flask, and Docker. For orchestration we rely largely on SLURM and
          Kubernetes with GitHub and GitHub Actions for source control and CI/CD.
          Increasingly, AI tools such as OpenAI/Azure Chat APIs, CoPilot, Codex, and
          LangChain/LangGraph are being integrated across the SDLC to enhance
          productivity and analysis capabilities.
        </p>
      </v-col>
    </v-row>
  </v-container>

  <v-container>
    <h2 class="text-h6 font-weight-bold mb-4">Highlighted Projects</h2>
    <v-row v-for="(proj, i) in featured" :key="proj.title" class="mb-4">
      <v-card
        class="mx-auto"
        :prepend-avatar="proj.img"
        :to="proj.link"
        :target="proj.link ? '_blank' : null"
        width="85%"
      >
        <template v-slot:title>
          <span class="font-weight-black">{{ proj.title }}</span><br />
          <span class="text-caption text-secondary">{{ proj.desc }}</span>
        </template>
        <v-card-text class="bg-surface-light pt-4">
          {{ proj.did }}
        </v-card-text>
      </v-card>
    </v-row>
  </v-container>

  <v-container>
    <h2 class="text-h6 font-weight-bold mb-4">Other Projects</h2>
    <v-expansion-panels multiple>
      <v-expansion-panel v-for="proj in others" :key="proj.title">
        <v-expansion-panel-title>
          <a :href="proj.link" target="_blank" class="text-decoration-none">{{ proj.title }}</a>
        </v-expansion-panel-title>
        <v-expansion-panel-text>{{ proj.desc }}</v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>
</template>
