<template>
    <div class="chat_box">
        <h4 class="chat_box_head">your chats </h4><hr />
        <ol class="list_container" v-for="i in users">
            <li class="list_cage">
                <img src="" class="user_image_for_container" />
                <div class="user_detail_in_container">
                    <p class="user_name_in_container">{{ i.name }}</p>
                    <p class="date_and_time">{{ dateTime }}</p>
                </div>
                <p class="user_msg_count">{{ i.msg_count }}</p>
                <div class="circle"></div>
            </li>
        </ol>
    </div>

    <table>
        <tr>
            <th>image</th>
            <th>name</th>
            <th>msg</th>
            <th>sts</th>
            <th>drop down</th>
        </tr>
        <tr>
            <td>img</td>
            <td>shyam</td>
            <td>3</td>
            <td>online</td>
            <td>go</td>
        </tr>
        <tr>
            <td>img</td>
            <td>shyam</td>
            <td>3</td>
            <td>online</td>
            <td>go</td>
        </tr>
    </table>
</template>

<script>
    export default {
        data() {
            return {
                users: [
                    { name: 'hari charan das', status_of_friend: false, msg_count: 20 },
                    { name: 'ram sing su sfsds', status_of_friend: true, msg_count: 40 },
                    { name: 'bindo bando', status_of_friend: true, msg_count: 50 }
                ],
                dateTime: '20.09.23:4.50 AM',
                //bgcolor : scolor
            }
        }
    }
</script>

<style scoped>
    .chat_box {
        border: 1px solid black;
        width: 20%;
    }
    .chat_box_head {
        padding-left: 2em;
    }
    .list_container {
        margin: 0px;
        padding: 0px;
        border-bottom: 1px solid black;
    }
    /*list_cage class*/
    .list_cage{
        display: flex;
        align-items:center;
        flex-direction: row;
        gap: .9em;
    }
    /*image of the user in chat box*/
    .user_image_for_container {
        height: 2.5em;
        width: 2.5em;
        border: 1px solid black;
    }
    /*user detail container */
    .user_detail_in_container {
        border: 1px solid black;
    }
    /*user name in the chat box*/
    .user_name_in_container {
        font-family: 'Global Monospace';
        color: black;
        font-size: 1em;
        position: relative;
        top: .3em;
        width: max-content;
    }
    /*date and time box for chat when the last time the msg is deliverd */
    .date_and_time {
        font-family: 'Global Monospace';
        position: relative;
        bottom: .5em;
        font-size: .7em;
    }
    /*user message count for the chat box */
    .user_msg_count{
        border:1px solid black;
        padding: 0em 1em 0em 1em;
    }
    /*circle for show the user status wheater it is offline or online in the chat box */
    .circle {
        border: 1px solid teal;
        outline: 1px solid teal;
        height: .3em;
        width: .3em;
        padding: .2em;
        background-color: teal;
        border-radius: 100%;
    }
</style>
