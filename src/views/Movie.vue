<script setup>
    import axios from 'axios'
    import MovieGenresCard from '@/components/MovieGenresCard.vue';
    
    import { reactive, onMounted, computed } from 'vue'

    const movies = reactive({})
    const media_genres = reactive({})
    

    onMounted(async () => {
        const response_m = await axios.get('http://localhost/api/movies')
        movies.value = response_m.data

        const response_mg = await axios.get('http://localhost/api/mediagenre')
        media_genres.value = response_mg.data
    })


    /* slidecontainer = scroll-snap-type: x mandatory;
        slide scroll-snap-align: start;
        */

</script>

<template>

    
    <v-container class="bg-[#263537]">
        <h2>Fugiat</h2>
        <div v-for="media_genre in media_genres.value">
            <div v-if="media_genre.genre_id === 1 && media_genre.id <= 10">
                <div v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Ipsam et</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 2 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Cumque</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 3 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>In autem</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 4 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Qui</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 5 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Dolores</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 6 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Omnis</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 7 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Mollitia</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 8 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Fuga qui</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 9 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

        <h2>Corrupti</h2>
        <div class="catalogue-container" v-for="media_genre in media_genres.value">
            <div class="slide-container" v-if="media_genre.genre_id === 10 && media_genre.id <= 10">
                <div class="slide" v-for="movie in movies.value">
                    <MovieGenresCard v-if="movie.media.id === media_genre.id" 
                    :title="movie.media.title" 
                    :duration="movie.duration"
                    :cover="movie.media.cover" />
                </div>
            </div>
        </div>

    </v-container>

    
</template>

<style scoped>

    h2{
        font-size: 14px;
        margin-right: 10px;
        font-style: italic;
        color:#EBF8F8;
    }

    .catalogue-container{
        width: 100%;
        margin: auto;
        overflow-x: auto;
    }

    .slide-container{
        display: flex;
        flex-direction: column;
        -webkit-overflow-scrolling: touch;
        white-space: nowrap; 
    }

    .slide{
        width: 100%;
        flex: 0 0 auto;
        white-space: normal;
        padding: 0 10px;
        box-sizing: border-box;
    }
    
</style>