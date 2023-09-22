<template>
    <div class="utility">
        <a class="notification"><div class="circle"></div></a>
        <a class="setting"><img src="public/setting.gif" alt="image link" /></a>
    </div>
</template>

<script>

</script>

<style scoped>
    .utility{
        display: flex;
        gap: .5em;
        border: 1px solid black;
    }
    .utility a:hover{
     
    }
    .utility a .circle{
        padding: .5em;
        border: .1px solid black;
        border-radius: 50%;
        position: relative;
        top: .6em;
    }
    .utility .setting img{
         max-height: 2em;
         max-width: 2em;
         position: relative;
         top: .2em;
    }

</style>