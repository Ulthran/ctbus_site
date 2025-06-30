<script setup>
import BlogHero from '../components/BlogHero.vue'
import posts from '../data/posts.js'
const slug = 'comps'
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
    <!-- Plotly -->
    <script src="https://cdn.plot.ly/plotly-2.26.0.min.js" integrity="sha384-xuh4dD2xC9BZ4qOrUrLt8psbgevXF2v+K+FrXxV4MlJHnWKgnaKoh74vd/6Ik8uF" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js" integrity="sha512-vc58qvvBdrDR4etbxMdlTt4GBQk1qjvyORR2nrsPsFPyrs+/u5c3+1Ct6upOgdZoIl7eq6k3a1UPDSNAQi/32A==" crossorigin="anonymous"></script>
    <!-- MathJax -->
    <script type="text/x-mathjax-config">
    MathJax = {
    tex: {
    inlineMath: [['$', '$'], ["\\(", "\\)"]],
    processEscapes: true,
    }
    }
    </script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6" integrity="sha384-WSLBwI+Q8tqRHaC+f1sjS/FVv5cWp7VAfrGB17HLfZlXhbp5F/RPVP7bYVHtiAWE" crossorigin="anonymous"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" integrity="sha384-Wuix6BuhrWbjDBs24bXrjf4ZQ5aFeFWBuKkFekO2t8xFU0iNaLQfp2K6/1Nxveei" crossorigin="anonymous"></script>
    <p >My undergraduate thesis project on physical reservoir computing models. In the paper I introduce the reservoir computing framework, necessary grounding in ML, the characteristics of good physical reservoirs, and a few case studies: mechanical, electronic, and quantum. While this is still a relatively new field, the potential for chaotic systems prediction, smart mechanical sensors and more is potentially revolutionary across a wide range of sciences and industries. I also gave a talk that mimics the structure of the paper.</p>
    <p >The phenomenon of reservoir computing arises from an amazing property of chaotic systems: that when you link two similar chaotic systems, they start to align with each other. The technical definitions of most of the words used there can vary across contexts but at its core, that is reservoir computing. It's creating a chaotic system you know and using it to extract information from one you don't.</p>
    <h3 >Linked Lorenz Systems</h3>
    <p >The Lorenz system is a classic example of a chaotic system. It's described by a set of three differential equations that dictate the evolution of the system in 3D space. The equations are:</p>
    <p >$$\frac{\delta x}{\delta t} = \sigma (y - x)$$ $$\frac{\delta y}{\delta t} = x (\rho - z) - y$$ $$\frac{\delta z}{\delta t} = x y - \beta z$$</p>
    <p >In the below plots, we can see chaotic system coupling in action. There are three Lorenz systems being simulated with the same parameters but the two on the right have different inputs from the one on the left. Additionally, the linked attractor #2 has one dimension of its evolution partially defined by attractor #1. This can be simulated according to the following equations:</p>
    <p >$$x_{1,t} = x_{1,t-1} + dx * dt$$ $$y_{1,t} = y_{1,t-1} + dy * dt$$ $$z_{1,t} = z_{1,t-1} + dz * dt$$</p>
    <p >$$x_{2,t} = x_{2,t-1} + dx * dt$$ $$y_{2,t} = (1 - c)(y_{2,t-1} + dy * dt) + c * y_{1,t-1}$$ $$z_{2,t} = z_{2,t-1} + dz * dt$$ $$c = 0.03$$</p>
    <p >$$x_{3,t} = x_{3,t-1} + dx * dt$$ $$y_{3,t} = y_{3,t-1} + dy * dt$$ $$z_{3,t} = z_{3,t-1} + dz * dt$$</p>
    <a onclick="hide_unhide_plots()" >Hide/Show Lorenz Plots</a>
    <div  id="LorenzPlots">
    <div id='Lorenz' ><!-- Plotly chart will be drawn inside this DIV --></div>
    <div id='Lorenz_unlinked_2'><!-- Plotly chart will be drawn inside this DIV --></div>
    <div id='Lorenz2'><!-- Plotly chart will be drawn inside this DIV --></div>
    <script>
    function hide_unhide_plots() {
    var x = document.getElementById("LorenzPlots");
    if (x.style.display === "none") {
    x.style.display = "flex";
    } else {
    x.style.display = "none";
    }
    }
    </script>
    <script src=""></script>
    <p >Each dot represents its own version of the system (unique starting points) and you can see from the highlighted red one that the dots across the two linked systems are drawn to each other and, even if they aren't always on the same side of the attractor, quickly fall into the same (quasi-)period. Meanwhile the unlinked system is doing its own thing, on its own time. And this is with a coupling constant of only 0.03!</p>
    <h3 >More Systems</h3>
    <p >The Mackey-Glass system is a single variable : $$\frac{dx}{dt} = \frac{\beta x(t-\tau)}{1+x(t-\tau)^n} - \gamma x(t)$$</p>
    <div id="MG" ><!-- Plotly chart will be drawn inside this DIV --></div>
    <script src=""></script>
    <p >It is a time delayed system, which means it relies on previous values of itself to determine its present dynamics. It is inspired by biological systems and is also the model used by <a href="https://www.nature.com/articles/ncomms1476" target="_blank" >L. Appeltant in his thesis work developing the first example of a physical system being used for reservoir computing</a>. He (and later in a class taught by <a href="https://umdphysics.umd.edu/people/faculty/current/item/445-rroy.html" target="_blank" >Rajarshi Roy</a>, I) mimicked this sytem's dynamics with a nonlinear, optoelectronic circuit to act as a physical reservoir computer.</p>
    <p >In the paper I also explore a mechanical system being used as a reservoir (a bunch of masses and springs) and a quantum computer being used as a reservoir. Maybe I'll write more about those here in the future.</p>
  </v-container>
</template>
