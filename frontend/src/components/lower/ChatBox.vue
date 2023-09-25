<template>
    <div class="chats">
        <h4>chats:</h4><hr />
        <ol class="list_container">
            <li v-for="i in names" class="list_of_names">{{ i }}</li>
        </ol>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                names : ['chat names', 'ram', 'hari', 'jadu']
            }
        }
    }
</script>

<style scoped>
    .chats{
        border: 1px solid black;
        width: 20%;
    }
    .chats .list_container{
        margin: 0px;
        padding: 0px;
    }
    .list_of_names {
        list-style-type: none;
        border-bottom: 1px solid black;
        padding: .5em;
    }
</style>