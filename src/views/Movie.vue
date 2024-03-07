<script setup>
    import axios from 'axios'
    import MovieGenresCard from '@/components/MovieGenresCard.vue';
    
    import { reactive, onMounted, computed } from 'vue'

    const genres = reactive({})
    const movies = reactive({})
    const media_genres = reactive({})
    const medias = reactive({})


    onMounted(async () => {
        const response_g = await axios.get('http://localhost/api/genre')
        genres.value = response_g.data

        const response_m = await axios.get('http://localhost/api/movies')
        movies.value = response_m.data

        const response_mg = await axios.get('http://localhost/api/mediagenre')
        media_genres.value = response_mg.data

        const response_me = await axios.get('http://localhost/api/media')
        medias.value = response_me.data
    })

</script>

<template>

    
    <v-container class="bg-[#263537]">
        <h1>Fugiat.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 1 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Ipsam et.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 2 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Cumque.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 3 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>In autem.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 4 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Qui.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 5 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Dolores.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 6 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Omnis.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 7 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Mollitia.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 8 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Fuga qui.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 9 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h1>Corrupti.</h1>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 10 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :description="movie.media.description" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

    </v-container>

    
</template>

<style scoped>
    .cards{
        overflow-x: auto;
        white-space: nowrap;
    }
</style>