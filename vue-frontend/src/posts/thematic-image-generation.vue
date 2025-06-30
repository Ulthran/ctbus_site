<script setup>
import BlogHero from '../components/BlogHero.vue'
const posts = window.posts
const slug = 'thematic-image-generation'
const info = posts[slug]
</script>

<template>
  <BlogHero
    :title="info.title"
    :subtitle="info.subtitle"
    :date="info.date"
    :tags="info.tags"
    :img="`CDN_URL/images/blog/${slug.replace(/-/g, '_')}.png`"
  />
  <v-container class="py-4">
    <p >I recently moved some things around on my site to have this Blog separate from the <a  href="" target="_blank">Projects</a> page. And as part of this move, I wanted to make the Blog look nice by having a little thumbnail art for each post, so I set to work in the AWS Bedrock Playground.</p>
    <p >I had some rough idea of what I wanted the general style of the designs to be, but no good examples. As I started generating images I quickly came to a few realizations. 1) Image generators love putting text from your prompt in the image. You can include negative prompts like "NO WORDS. NO TEXT." but they still resist. 2) If you want a precise style for your output you better be able to describe that style VERY precisely in addition to the content of the image. Any vagueries will allow the model to explore any number of ideas you don't necessarily want. 3) They love generating DNA helixes backwards. Always check your images for reality if that's something that matters to your application.</p>
    <p >By far the best technique for generating the image you want is iterative generation. In the AWS Bedrock Playground it's super easy. Start by prompting it to generate an image and when, most likely, you're disappointed with the results, take the best looking one and select Generate Variation. Then you can modify your prompt, explain changes you want to see, and set it off again. After enough of these iterations, you can actually achieve pretty impressive results.</p>
    <p >But I didn't want to go through this process each time I make a blog post. For one thing, it's more expensive than a single generation. For another, it's much harder to arrive at consistent styles. You can achieve impressive results separately but when you put them together they don't always look cohesive, because they might have taken such different paths to generate. So instead I generated a few seed images. In essence, I pursued iterative generation until I got a few images that were the exact style I was going for, a kind of medieval pixel art with plants in my case, and now I can use those seeds to create new thumbnails. Each new post I write, I generate images with a mix of a seed image and a prompt just giving a few words or ideas to push it towards the post content (the thumbnail for this post is one of the seed images).</p>
    {
    "model-id": "amazon.titan-image-generator-v2:0",
    "action": "generate-variations",
    "image-size": "384x576",
    "seed-image": "seed.png",
    "prompt-strength": 8,
    "similarity-strength": 0.5,
    }
  </v-container>
</template>
