<template>  
    <div class="compname">
        <p>DateApp</p>
        <img src="/thita1.jpg" alt="image" class="spin_image"/>
<!--size of the image is 100 by 58 in pixel-->
    </div>
</template>
<style scoped>
    .compname {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: .4em;
    }
    .compname p{
        padding-left: .5em;
    }
    .compname img{
        height: 1em;
        width: auto;
        display: flex;
        align-items: center;
        filter: brightness(1)
    }

    @keyframes spin {
        0% {
            transform: rotateY(0deg);
        }

        100% {
            transform: rotateY(360deg);
        }
    }
    .spin_image {
        animation: spin 4s linear infinite;
    }

</style>