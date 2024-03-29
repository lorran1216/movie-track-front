<script setup>
import {ref, reactive} from 'vue'
import axios from 'axios'

const name = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref("")


const handleSubmit = async() =>{
    console.log("clicked")
    if(password != confirmPassword){
        return;
    }

    try{
        const response = await axios.post('http://localhost/api/users', {
            name: name.value,
            email: email.value,
            password: password.value
        });
        console.log(response.data);
    }catch(error){
        console.error('Error: ', error);
    }
}
</script>


<template>
    <v-container class="container">
        <form @submit.prevent="handleSubmit" class="from">
            <div>

                <label for="name">Name</label>
                <input v-model="name" class="text" id="name" name="name" type="text" placeholder="Type your name">

                <label for="email">E-mail</label>
                <input v-model="email" class="text" id="email" name="email" type="email" placeholder="example@example.com">
                
                <label for="password">Password</label>
                <input v-model="password" class="text" id="password" name="password" type="password" placeholder="*********">
                
                <label for="confirm_password">Confirm password</label>
                <input v-model="confirmPassword" class="text" id="confirm_password" name="confirm_password" type="password" placeholder="*********">
            </div>

            <div v-if="password != confirmPassword">
                <h3>Passwords doesn't match</h3>
            </div>

            <div class="flex-row">
                <h2><a href="/signin">Already have an account?</a></h2>
                <button type="submit" class="btn">Sign up</button>
            </div>
        </form>
    </v-container>
</template>

<style scoped>

    .container{
        display: flex;
        height: 100vh;
        width: 100vw;
        justify-content: center;
        align-items: center;
        background-color: #263537;
    }

    form{
        display:flex;
        flex-direction: column;
        width: 65vw;
        align-items: center;
    }

    .text{
        margin: 0px;
        border: solid 1px black;
        border-radius: 5px;
        width: 273px;
        height: 32px;
        background-color: #EBF8F8;
    }

    .btn{
        background-color: #93DDE0;
        border: solid 1px #93DDE0;
        border-radius: 5px;
        width: 100px;
    }

    .flex-row{
        display: flex;
        margin-top: 16px;
    }

    h2{
        font-size: 14px;
        margin-right: 10px;
        font-style: italic;
        color:#EBF8F8;
    }

    label{
        font-style: italic;
        color:#EBF8F8;
    }
</style>