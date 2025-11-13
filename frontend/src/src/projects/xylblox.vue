<script setup>
import ProjectHero from "../components/ProjectHero.vue";
const projects = window.projects;

const info = projects["xylblox"];
</script>

<template>
  <ProjectHero
    :title="info.title"
    :subtitle="info.subtitle"
    :tags="info.tags"
    :img="`ASSETS_BASE_URL/images/${info.image}`"
  />
  <v-container>
    <v-card class="mb-4">
      <v-card-title>Overview</v-card-title>
      <v-card-text>
        This is as much a passion project as a viable business idea. I've spent
        way too many hours through my life playing Minecraft and multiplayer is
        always a pain (especially if you're cheap and don't want to pay for
        monthly hosting plans). Xylblox started simply as me building a robust
        Minecraft hosting architecture on AWS for me and some friends to play.
        As I did that, I realized there is a real opportunity to create a
        product that doesn't exist on the Minecraft hosting market: a true
        pay-per-usage model. Everyone else charges flat monthly fees that rely
        on overprovisioning and customer inertia to make money. I can build
        something that is more cost effective and doesn't prey on customers'
        absentmindedness. It's still early days, but I'm excited to keep
        building this out.
      </v-card-text>
    </v-card>

    <v-card>
      <v-card-title>Links</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="auto">
            <a href="https://xylblox.com" target="_blank" title="Xylblox Site">
              <v-btn variant="text" icon>
                <i class="fas fa-globe"></i>
              </v-btn>
            </a>
          </v-col>
          <v-col cols="auto">
            <a
              href="https://github.com/Ulthran/minecraft_for_all"
              target="_blank"
              title="GitHub Repo"
            >
              <v-btn variant="text" icon>
                <i class="fab fa-github"></i>
              </v-btn>
            </a>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-container>
</template>
