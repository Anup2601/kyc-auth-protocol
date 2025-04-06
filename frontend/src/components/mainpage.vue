<template>
  <div class=" mainb flex-1 flex flex-col">
    <!-- Nav Bar -->
    <header class="bg-white shadow p-4 flex justify-between items-center">
      <h1 class="heading text-lg font-semibold">Martin Maverick </h1>
      <nav class="navbar">
        <span class="sidetab" v-for="(tab, index) in tabs2" :key="index">
          <button
            @click="activeTab = tab.name"
            :class="['sidebar-tab', { active: activeTab === tab.name }]"
          >
            {{ tab.label }}
          </button>
        </span>
      </nav>
    </header>


    <!-- Main Content -->
    <div class="flex h-screen">
      <!-- Sidebar -->
      <aside class="w-64 bg-gray-800 text-white flex flex-col">
        <div class="heading p-4 text-xl font-bold border-b border-gray-700 flex items-center justify-between">
          <span></span>
        </div>
        <div>
          <button
            @click="toggleSidebar"
            class="heading rotate-button focus:outline-none transition-transform duration-300 text-white text-xl"
          >
            <span :class="{ 'transform rotate-180 inline-block': !showSidebar }">&gt;</span>
        </button>
        </div>

        <!-- Expanded Sidebar -->
        <nav v-if="showSidebar" class="transition-all duration-200 sidebar flex-1 overflow-y-auto">
          <div class="sidetab" v-for="(tab, index) in tabs1" :key="index">
            <button
              @click="activeTab = tab.name"
              :class="['sidebar-tab', { active: activeTab === tab.name }]"
            >
              {{ tab.label }}
            </button>
          </div>
        </nav>

        <!-- Collapsed Sidebar with Icons Only -->
        <nav v-else class="transition-all duration-200 sidebar flex-1 overflow-y-auto text-center">
          <div class="sidetab" v-for="(tab, index) in tabs1" :key="index">
            <button
              @click="activeTab = tab.name"
              :class="['sidebar-tab', { active: activeTab === tab.name }]"
              title="tab.label"
            >
              <span class="text-2xl">{{ tab.icon }}</span>
            </button>
          </div>
        </nav>
        
      </aside>

      <!-- Sub Page Area -->
      <main class="subspace flex-1 overflow-y-auto p-6">
        <component :is="getComponent(activeTab)" />
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Dashboard from '../components/Dashboard.vue'
//import Tab2 from './components/Tab2.vue' {{ activeTab }}
//import Tab3 from './components/Tab3.vue'
//import Tab4 from './components/Tab4.vue'
//import Tab5 from './components/Tab5.vue'
//import Tab6 from './components/Tab6.vue'
//import Tab7 from './components/Tab7.vue'
//import Tab8 from './components/Tab8.vue'
//import Tab9 from './components/Tab9.vue'
//import Tab10 from './components/Tab10.vue'

const showSidebar = ref(true)

function toggleSidebar() {
  showSidebar.value = !showSidebar.value
}


const tabs1 = [
  { name: 'Dashboard', label: 'Dashboard', icon: '📊' },
  { name: 'Tab2', label: 'Leads', icon: '🧲' },
  { name: 'Tab3', label: 'Contacts', icon: '📇' },
  { name: 'Tab4', label: 'Accounts', icon: '🏦' },
  { name: 'Tab5', label: 'Opportunities', icon: '💼' },
  { name: 'Tab6', label: 'Activities', icon: '📆' },
  { name: 'Tab7', label: 'Campaigns', icon: '📢' },
  { name: 'Tab8', label: 'Reports', icon: '📑' },
  { name: 'Tab9', label: 'Settings', icon: '⚙️' },
  { name: 'Tab10', label: 'Help', icon: '❓' },
]
const tabs2 = [
  { name: 'Home', label: 'Home', icon: '📊' },
  { name: 'Profile', label: 'Profile', icon: '📇' },
  { name: 'Logout', label: 'Logout', icon: '🧲' },
]

const activeTab = ref('Dashboard')

function getComponent(tabName) {
  return {
    Dashboard,    //Tab2,    Tab3,    Tab4,    Tab5,    Tab6,    Tab7,    Tab8,    Tab9,    Tab10,
  }[tabName]
}
</script>

<style scoped>
@import "tailwindcss";

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #1f2937;
}

.mainb {
  height: 100vh;
  background-color: #1f2937;
}
.navbar{
  padding: 0px;
  font-size: 1.5rem;
  font-weight: 600;
  border-right: 1px solid #4a5568;
  background-color: #1f2937; /* Dark gray for sidebar */
  height: 100%;
  display: flex;
  flex-direction: row;
}

.heading {
  padding: 3px;
  font-size: 2rem;
  font-weight: bold;
  text-align: center;
  color: #e2e8f0; /* Darker shade */
}

.subspace {
  background-color: #f9fafb; /* Very light gray */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.sidebar {
  padding: 0px;
  font-size: 1.5rem;
  font-weight: 600;
  border-right: 1px solid #4a5568;
  background-color: #1f2937; /* Dark gray for sidebar */
  height: 100%;
}

.sidebar button, .navbar button {
  width: 100%;
  text-align: left;
  padding: 0.5rem 0.5rem;
  margin-bottom: 0.4rem;
  border-radius: 5px;
  background-color: transparent;
  color: #e2e8f0; /* Light text */
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
[v-cloak] {
  display: none;
}
[v-else] .sidebar button {
  justify-content: center;
}


.sidebar button:hover {
  background-color: #374151; /* Slightly lighter on hover */
  color: #ffffff;
}

.sidebar button.active {
  background-color: #3b82f6; /* Blue for active */
  color: white;
}
.rotate-button {
  transition: transform 0.3s ease;
}

.rotate-180 {
  transform: rotate(0deg);
}
</style>
