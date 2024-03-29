<script setup>
    import axios from 'axios'
    import MovieCard from '@/components/MovieCard.vue';
    import MenuBar from '@/components/MenuBar.vue';
    
    import { reactive, onMounted, ref, computed } from 'vue'

    const movies = reactive({})
    const media_genres = reactive({})
    const genres = reactive({})

    

    const movis = computed( () => {
        return movies?.value?.filter((movie) => movie.duration < 200)
    })

    const med1 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 1)
    })

    const med2 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 2)
    })

    const med3 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 3)
    })

    const med4 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 4)
    })

    const med5 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 5)
    })

    const med6 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 6)
    })

    const med7 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 7)
    })

    const med8 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 8)
    })

    const med9 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 9)
    })

    const med10 = computed( () => {
        return media_genres?.value?.filter((media) => media.genre_id === 10)
    })

    console.log(movis)
    onMounted(async () => {
        const response_m = await axios.get('http://localhost/api/movies')
        movies.value = response_m.data

        const response_g = await axios.get('http://localhost/api/genre')
        genres.value = response_g

        const response_mg = await axios.get('http://localhost/api/mediagenre')
        .catch((error) => {
            console.log(error)
        })

        media_genres.value = response_mg.data
    })
    
</script>

<template>

    
    <v-container class="bg-[#263537]">

        <h2 style="margin-bottom: 1px;">{{genres.value.data[0].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med1" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[1].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med2" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>
        
        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[2].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med3" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[3].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med4" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[4].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med5" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[5].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med6" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[6].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med7" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[7].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med8" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[8].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med9" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

        <hr>
        <br />

        <h2 style="margin-bottom: 1px;">{{genres.value.data[9].name}}</h2>
        <div style="overflow-x: auto; white-space: nowrap;" >
            <div v-for="media in med10" style="display: inline-block;">
                <div v-for="movie in movies.value" style="display: inline-block; margin-right: 1px;">
                    <MovieCard v-if="movie.media.id === media.id"
                    :title = movie.media.title
                    :duration = movie.duration
                    />
                </div>
            </div> 
        </div>

    </v-container>
    <MenuBar/>

    
</template>

<style scoped>
</style>