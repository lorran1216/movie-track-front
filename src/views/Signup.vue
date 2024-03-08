<template>
    <v-container class="container">
        <form class="from">
            <div>
                <label for="email">E-mail</label>
                <input class="text" id="email" name="email" type="email" placeholder="example@example.com">
                
                <label for="password">Password</label>
                <input class="text" id="password" name="password" type="password" placeholder="*********">
                
                <label for="confirm_password">Confirm password</label>
                <input class="text" id="confirm_password" name="confirm_password" type="password" placeholder="*********">
            </div>

            <div class="flex-row">
                <h2>Already have an account?</h2>
                <button class="btn">Sign up</button>
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