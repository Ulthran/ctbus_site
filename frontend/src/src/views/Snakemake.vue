<template>
  <v-container>
    <h1>Snakemake Demo</h1>
    <p>
      Use the embedded JupyterLite environment to run a simple Snakemake
      workflow directly in your browser.
    </p>
    <p>Try this example in the notebook:</p>
    <pre><code>import micropip, pathlib, textwrap
await micropip.install("snakemake")

pathlib.Path("data.txt").write_text("A\nB\n")
pathlib.Path("Snakefile").write_text(textwrap.dedent("""rule count:
  input: "data.txt"
  output: "count.txt"
  shell: "wc -l {input} > {output}"
"""))

!snakemake
</code></pre>
    <iframe
      src="https://jupyterlite.github.io/demo/lab/index.html"
      style="width: 100%; height: 800px; border: 1px solid #ccc"
    ></iframe>
  </v-container>
</template>

<script>
export default {
  name: "Snakemake",
};
</script>
