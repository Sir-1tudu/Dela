<template>
    <div class="chats">
        <h4 class="head">your friends </h4><hr />
        <ol class="list_container" v-for="i in users">
            <li class="list_of_names">{{ i.name }}</li>
            <li class="status">{{ i.status_of_friend }}</li>
            <li class="message_count">{{ i.msg_count }}</li>
        </ol>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                users: [
                    { name: 'hari', status_of_friend: false, msg_count: 20 },
                    { name: 'ram', status_of_friend: true, msg_count: 40 },
                    { name: 'bindo', status_of_friend: true, msg_count: 50 },
                ]
            }
        }
    }
</script>
<style scoped>
    .chats{
        border: 1px solid black;
        width: 20%;
    }
    .chats .head{
        padding-left: 2em;
    }
    .chats .list_container{
        margin: 0px;
        padding: 0px;
        display: flex;
        gap: .5em;
        border-bottom: 1px solid black;
    }
    .list_of_names {
        list-style-type: none;
        padding: .5em;
    }
    .status {
        list-style-type: none;
        padding: .5em;
    }
    .message_count {
        list-style-type: none;
        padding: .5em;
    }
</style>
