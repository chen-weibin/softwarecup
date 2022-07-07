<template>
    <div class="progress">
        <div class="main">
            <div class="solid" :style="style"></div>
        </div>
        <div class="person">{{percent}}</div>
    </div>
</template>

<script>
    export default {
        name: 'Progress',
        props: {
            current: {
                type: Number,
                required: true
            }
        },
        computed: {
            style(){
                const percent = this.current + '%'
                return {
                    width: percent
                }
            },
            percent() {
                return parseInt(this.current) + '%'
            }

        }
    }
</script>

<style lang='less' scoped>
    .progress {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .main {
        width: 85%;
        height: 8px;
        border-radius: 4px;
        background-color: #e7e7e7;
        position: relative;
        overflow: hidden;
    }
    .solid {
        position: absolute;
        top: 0;
        left: 0;
        width: 20px;
        height: 100%;
        background-color: #7399ff;
        transition: all ease-out .5s;
    }
    .person {
        padding-left: 12px;
        font-size: 11px;
        color: var(--main-font-color);
    }
</style>