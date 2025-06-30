<script setup>
import SimplePage from '../components/SimplePage.vue'
</script>

<template>
  <SimplePage title="Serverless Dashboards with Dash">
    <p >Up until recently, I had a (janky) Spotify stats visualizer on this site that I had implemented with Flask handling the backend and a simple JavaScript frontend. It wasn't particularly well organized code, especially on the frontend and I wanted to move it to a separate repository. So with the dual goals of trying to offload this bad code and get more practice with AWS SAM, I set about implementing a super simple serverless dashboard.</p><br />
    <p >The finished GitHub repository can be found <a  href="https://github.com/Ulthran/spotify_vis" target="_blank">here</a> and the live site <a  href="https://0qn7o9e6pd.execute-api.us-east-1.amazonaws.com/Prod/" target="_blank">here</a>.</p>
    <p >Going from nothing to having an active serverless data dashboard is a pretty quick process once you know what tools you want to use. In our case, that's the SAM CLI, Dash, Spotipy, and TailwindCSS. Then it's just five steps:</p><br />
    <p >1. Initialize a new SAM app using the SAM CLI and a Python runtime.</p>
    <p >2. Make a new file called <i>dash_app.py</i> in which you implement your Dash app.</p>
    <p >3. Make a new file called <i>spotipy.py</i> in which you implement a singleton class for authenticating to the Spotify API and getting data.</p>
    <p >4. Include Tailwind via a CDN link and apply style classes to Dash app components.</p>
    <p >5. Build and deploy your app using the SAM CLI.</p><br />
    <p >For reference on any of the above steps, check out the GitHub (linked above). I've tried to break it down in such a way that you could replace any component of the tech stack with another of your choice, for example if you wanted to style with Bootstrap (Tailwind -> Bootstrap) or if you wanted to see real-time stats on your Instagram usage (Spotipy -> HikerAPI).</p>
    <p >One piece of the puzzle that I glossed over but is non-trivial is how to define the <i>lambda_handler</i> in <i>app.py</i>. The difference lies in how the app handles custom domains vs API Gateway assigned ones. If you know you'll only use API Gateway assigned domains, you can simplify the event handler. On the bright side, you should be able to just copy/paste what I've written into any project and have it work.</p>
    <p >Unfortunately, Spotify recently removed public access to most of the fun stats they keep on a per-song basis. Things like tempo, key, "danceability," and "speechiness" are now too valuable for training the Recommendation Algorithm to expose, leaving my dashboard with little to show beyond popularity and playtimes. Still, from a technical perspective, there is a major improvement to be made, which you'll probably notice if you visit the site: the initial page load time is super slow. This should be a relatively simple fix, as SAM provides tooling for keeping functions warm!</p><br />
    <p >Expect another blog post soon about a similarly simple serverless data dashboard, this time implemented with Streamlit!</p>
  </SimplePage>
</template>
