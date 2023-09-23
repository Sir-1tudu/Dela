<template>
    <div id="top_bar">
        <com-image />
        <search-box />
        <utility-box />
    </div>
    <hr />
    <div id="bottom">
        <chat-box />
        <div id="middle">content</div>
        <div id="right">
            <div id="settings">settings</div>
            <div id="chat">chat</div>
        </div>
    </div>

</template>

<script>

</script>
<style scoped>
    #top_bar {
        background: linear-gradient(to right, skyblue, teal);
        /*border: 1px solid black;
/*        border-radius: .3em;*/
/*        box-shadow: 1px 1px 8px black;*/
/*        padding: .1em;*/
        display: flex;
        gap: 1em;
        padding: 0px;
    }
    #bottom{
        display:flex;
        flex-direction: row;
        gap: 1em;
    }
</style>