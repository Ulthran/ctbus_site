<script setup>
import BlogHero from '../components/BlogHero.vue'
import posts from '../data/posts.js'
const slug = 'firewalls-in-china'
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
    <p >In the fall of 2019, I spent four months studying Mandarin in Harbin, China with <a href="https://cetacademicprograms.com/college-study-abroad/programs/china/harbin-chinese-language/" target="_blank" >CET</a> and the <a href="http://en.hit.edu.cn/" target="_blank" >Harbin Institute of Technology</a> (HIT). As part of the program, I was able to design a 1-on-1 class with a HIT professor and chose to do it on computer networks and their security (particularly relevant in China, where there is a nationwide firewall preventing access to certain parts of the internet). The end result was a three page paper summarizing the course's content and a number of shorter intermediate papers going into detail on each week's subject.</p>
    <h3 >Why'd You Do This?</h3>
    <p >I had taken Latin for five years previously (7th - 11th grades) but didn't have room for it in my schedule senior year of high school so figured it was time for a change of pace when I got to college. I started taking Chinese and ended up taking a Chinese class for eight of my twelve terms at Carleton (we did trimesters). This includes the fall of Junior year (about half a year before Covid came to the United States) when I did a semester abroad in Harbin, China, which is the northernmost city with a population over five million in China. The program involved developing an independent study type of class, in addition to three other classes, all taught in Chinese and we were only allowed to speak Chinese unless calling our families.</p>
    <h3 >How'd it Go?</h3>
    <p >There's no question that the main challenge of the classes was the language and not the content. Even so, I got a fairly solid overview of the field of network security. I had initially intended to delve more into the Great Firewall itself but I think, especially given the geopolitical climate at the time, my professor astutely avoided that topic. We started by going over relevant concepts of computer networks and some foundational technologies. From there we got into how networks can be segmented and how access can be controlled. This lead into learning about some firewall types, what they protect against, and a little bit of how they can be exploited.</p>
    <p >Despite the lack of technical depth in the course, there were new concepts I was introduced to and for a while afterwards whenever I tried to think or talk about them it would come up in Chinese. Unfortunately at this point it's been a few years since I've spoken or read/written any Chinese and most of it no longer comes naturally. Maybe someday I'll have reason to revive it.</p>
  </v-container>
</template>
