<script setup>
import Hero from '../components/Hero.vue'
const CDN_URL = window.CDN_URL || ''

const featured = [
  {
    title: 'Sunbeam',
    link: 'https://github.com/sunbeam-labs/sunbeam',
    img: `${CDN_URL}/images/sunbeam_logo.png`,
    desc: 'A robust and extensible Snakemake pipeline for metagenomic sequencing analysis.',
  },
  {
    title: 'Condabot',
    link: 'https://github.com/sunbeam-labs/condabot',
    img: `${CDN_URL}/images/condabot_logo.png`,
    desc: 'Automates dependency updates for Conda environments across our projects.',
  },
  {
    title: 'sbx_template',
    link: 'https://github.com/sunbeam-labs/sbx_template',
    img: `${CDN_URL}/images/sunbeam_logo.png`,
    desc: 'Template repository for quickly creating new Sunbeam extensions.',
  },
  {
    title: 'Autobfx',
    link: 'https://github.com/Ulthran/autobfx',
    img: `${CDN_URL}/images/autobfx_logo.png`,
    desc: 'A modern pipeline framework providing an alternative to Snakemake.',
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
  <Hero title="Developer in Statistical Metagenomics with the PCMP" />

  <v-container class="text-left">
    <details class="mb-2">
      <summary>What is Metagenomics?</summary>
      <p>If genetics is the study of individual genes and genomics the study of whole genomes, metagenomics looks at collections of genomes. The human gut microbiome, my main focus, is a prime example.</p>
    </details>
    <details class="mb-2">
      <summary>What exactly do you do?</summary>
      <p>As the software engineer for the PCMP I set development standards, refactor published work, and build internal services ranging from preprocessing automation to compute infrastructure.</p>
    </details>
    <details class="mb-2">
      <summary>What stack do you use?</summary>
      <p>Python is the language I use most, with R close behind. Pipelines rely on Snakemake and Prefect and run on a mix of HPC and AWS resources. We host code on GitHub and Enterprise GitHub with CI via GitHub Actions.</p>
    </details>
    <details class="mb-2">
      <summary>How do you use ML/AI?</summary>
      <p>Machine learning tools are integral to many of our analyses and I have begun experimenting with self‑hosted AI agents and knowledge bases to streamline research.</p>
    </details>
    <details class="mb-4">
      <summary>Can I see?</summary>
      <p>Absolutely! Highlighted projects are below with many more listed for further reading.</p>
    </details>
  </v-container>

  <v-container>
    <h2 class="text-h6 font-weight-bold mb-4">Highlighted Projects</h2>
    <v-row justify="center">
      <v-col cols="12" md="6" v-for="proj in featured" :key="proj.title">
        <v-card class="ma-2" :href="proj.link" target="_blank">
          <v-img v-if="proj.img" :src="proj.img" height="160" contain />
          <v-card-title>{{ proj.title }}</v-card-title>
          <v-card-text>{{ proj.desc }}</v-card-text>
        </v-card>
      </v-col>
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
