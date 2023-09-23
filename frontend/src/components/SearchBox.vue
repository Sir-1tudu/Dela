<template>
    <div class="search">
        <input type="search" placeholder="search your partner ..." class="box1"/>
        <input type="button" value="search" class="box2" />
    </div>
</template>

<style scoped>
    .search{
        display: flex;
/*        justify-content: center;*/
        align-items: center;
        gap: 2em;
        padding-left: 1em;
    }
    .box1{
        width: 75em;
        height: 3em;
        border: 1px solid teal;
        border-radius: 20px;
        padding-left: 2em;
        outline: none;
    }
    .box1:hover{
        outline: 1px solid teal;
    }
    .box1:active {
        outline: 1px solid teal;
    }
    .box1:after {
    outline: 1px solid teal;
    }
    .box2 {
        height: 3em;
        width: 5em;
        border: 1px solid teal;
        border-radius: 20px;
    }
    .box2:hover {
        outline: 1px solid teal;
        background: linear-gradient(to right, skyblue, teal);
    }

    .box2:active {
        outline: 1px solid teal;
    }

    .box2:after {
        outline: 1px solid teal;
    }

</style>