<script setup>
import SimplePage from '../components/SimplePage.vue'
const CDN_URL = window.CDN_URL || ''
</script>

<template>
  <SimplePage title="Start the Server">
    <br /><br />
    <button id="start-server"  onclick="startServer()">
    Start Server
    </button>
    <p id="loading-message" >Starting server... Go try it out.</p>
    <script>
    function startServer() {
    document.querySelector('#loading-message').classList.remove('hidden');
    document.querySelector('#start-server').disabled = true;
    fetch('https://f76p69rn87.execute-api.us-east-1.amazonaws.com/prod/start', {
    method: 'POST'
    })
    .then(response => response.text())
    .then(result => {
    console.log('Success:', result);
    //document.querySelector('#loading-message').textContent = 'Server started successfully! Wait a moment and then try to join.';
    })
    .catch(error => {
    console.error('Error:', error);
    //document.querySelector('#loading-message').textContent = 'Error starting server. Wait a moment and check to see if you can join anyways (this might be a temporary error). If not, let me know.';
    });
    }
    </script>
  </SimplePage>
</template>
