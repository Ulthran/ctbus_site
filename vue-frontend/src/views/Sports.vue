<script setup>
import SimplePage from '../components/SimplePage.vue'
import Badminton from '../svgs/Badminton.vue'
</script>

<template>
  <v-container class="d-flex flex-column align-center">
    <!-- Ultimate Frisbee -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Ultimate Frisbee</h2>
      <p class="text-body-1">I grew up on the sidelines of my parents' summer league games. Now I play for a club team that placed 5th in the northeast this year and has been a national champ in the past. I also play for the same summer league team my parents did (it's 40 years old!).</p>
      <v-row class="py-4" align="center" justify="space-around">
        <v-col cols="auto">
          <a href="https://www.buda.org/en_us/t/mob-3" target="_blank" title="M.O.B.: Hollaredutulliöh">
            <font-awesome-icon icon="bolt" style="width:48px;height:48px" />
          </a>
        </v-col>
        <v-col cols="auto">
          <a href="https://twitter.com/BruisesUltimate" target="_blank" title="Bruises: Compote ('19)">
            <font-awesome-icon icon="fist" style="width:48px;height:48px" />
          </a>
        </v-col>
        <v-col cols="auto">
          <a href="https://twitter.com/LoS_Ultimate" target="_blank" title="League of Shadows: You either die a hero or live long enough to see yourself become the villain ('21)">
            <font-awesome-icon icon="bat" style="width:48px;height:48px" />
          </a>
        </v-col>
        <v-col cols="auto">
          <a href="https://twitter.com/loco_ultimate" target="_blank" title="Loco: 1. 2. 3. 4. Loco. ('22)">
            <font-awesome-icon icon="train" style="width:48px;height:48px" />
          </a>
        </v-col>
        <v-col cols="auto">
          <a href="https://twitter.com/WildCardult" target="_blank" title="Wild Card: Uno, you know ('23)">
            <font-awesome-icon icon="uno-reverse" style="width:48px;height:48px" />
          </a>
        </v-col>
      </v-row>
    </v-card>

    <!-- Chess -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Chess</h2>
      <p class="text-body-1">Winter break, 2019, I came home and was sick for a week. So I played chess the whole time. And I've kept playing since (only sometimes getting better).</p>
      <v-row class="py-4" align="center" justify="space-around">
        <v-col cols="auto">
          <a href="https://www.chess.com/member/thwardenheimer" target="_blank" title="My Chess.com profile">
            <font-awesome-icon icon="chess" style="width:48px;height:48px" />
          </a>
        </v-col>
        <v-col cols="auto" class="d-flex flex-column align-center" title="Tactical puzzles are my favorite">
          <font-awesome-icon icon="puzzle-piece" style="width:24px;height:24px" />
          <p class="text-body-1 font-weight-bold">{{ chess.tactics }}</p>
        </v-col>
        <v-col cols="auto" class="d-flex flex-column align-center" title="Bullet">
          <BulletIcon style="width:24px;height:24px" />
          <p class="text-body-1 font-weight-bold">{{ chess.bullet }}</p>
        </v-col>
        <v-col cols="auto" class="d-flex flex-column align-center" title="Blitz">
          <font-awesome-icon icon="bolt" style="width:24px;height:24px" />
          <p class="text-body-1 font-weight-bold">{{ chess.blitz }}</p>
        </v-col>
        <v-col cols="auto" class="d-flex flex-column align-center" title="Rapid">
          <font-awesome-icon icon="stopwatch" style="width:24px;height:24px" />
          <p class="text-body-1 font-weight-bold">{{ chess.rapid }}</p>
        </v-col>
        <v-col cols="auto" class="d-flex flex-column align-center" title="Daily">
          <font-awesome-icon icon="sun" style="width:24px;height:24px" />
          <p class="text-body-1 font-weight-bold">{{ chess.daily }}</p>
        </v-col>
      </v-row>
    </v-card>

    <!-- Skiing -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Skiing</h2>
      <p class="text-body-1">I've skied the northeast my whole life and sometimes go out west just to feel worse about the conditions here.</p>
      <v-row class="py-4" align="center" justify="center">
        <v-col cols="auto">
          <font-awesome-icon icon="person-skiing" style="width:48px;height:48px" />
        </v-col>
      </v-row>
    </v-card>

    <!-- Soccer -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Soccer</h2>
      <p class="text-body-1">I played soccer until the end of high school and haven't had the time since. But I was awarded MVP of JV1 and JV2 my freshman year and MVDP (defensive player) of Varsity my senior year.</p>
      <v-row class="py-4" align="center" justify="center">
        <v-col cols="auto">
          <font-awesome-icon icon="futbol" style="width:48px;height:48px" />
        </v-col>
      </v-row>
    </v-card>

    <!-- Badminton -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Badminton</h2>
      <p class="text-body-1">I started playing badminton end of high school and trained 10 hours a week for a few months. Now I play for fun when I can.</p>
      <v-row class="py-4" align="center" justify="center">
        <v-col cols="auto">
          <font-awesome-icon icon="badminton" style="width:48px;height:48px" />
        </v-col>
      </v-row>
    </v-card>

    <!-- Squash -->
    <v-card class="mt-8 pa-4 text-center" max-width="600">
      <h2 class="text-h4 font-weight-bold mb-2">Squash</h2>
      <p class="text-body-1">I played squash for a few years somewhere around middle school. My crowning achievement was winning the Marblehead YMCA snowflake holiday tournament.</p>
      <v-row class="py-4" align="center" justify="center">
        <v-col cols="auto">
          <font-awesome-icon icon="squash" style="width:48px;height:48px" />
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>