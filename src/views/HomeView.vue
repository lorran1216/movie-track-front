<script setup>
import MovieCard from '../components/MovieCard.vue';
import MenuBar from '../components/MenuBar.vue';
import SearchBar from '../components/SearchBar.vue';
import axios from 'axios'
import { reactive} from 'vue'

const data = reactive({})
const filteredData = reactive({})
let searchItem = ''


const fetchData = async (page) => {
  const response = await axios.get('http://localhost/api/' + page)
  data.value = response.data
  filteredData.value = response.data
}


const filterByDuration = () => {
  if (!searchItem) {
    filteredData.value = data.value
    return
  }
  const durationFilter = parseInt(searchItem)
  filteredData.value = data.value.filter(item => item.duration < durationFilter)
}

const handleInput = (test) => {
  const [hours=0, mins=0] = test.split(':').map(Number)
  searchItem = hours * 60 + mins
  console.log(searchItem)
  filterByDuration()
}

</script>

<template>
  <SearchBar @search="handleInput"/>
  <v-container class="bg-[#263537]">
    <div v-for="movie in filteredData.value">
      <MovieCard 
        :title="movie.media.title" 
        :description="movie.media.description" 
        :duration="movie.duration" 
        :cover="movie.media.cover"
      />
    </div>
  </v-container>
  <MenuBar @changepage="fetchData"/>
</template>