<template>
    <div class="tipline">
        <ul>
            <li class="item" v-for="item in steps" :key="item.id">
                <div class="circle"></div>
                <div class="line" v-if="item.id !== steps.length"></div>
                <div class="tip">{{item.id}}. {{item.tip}}</div>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'TipLine',
        props: {
            steps: {
                type: Array,
                required: true
            }
        },
        
    }
</script>

<style lang='less' scoped>
    .tipline {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    ul {
        list-style: none;
        padding-top: 50px;
    }
    .item {
        position: relative;
        width: 220px;
        height: 85px;
        .circle {
            position: absolute;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            left: 0;
            top: 0;
            background-color: var(--change-tip-circle);
            z-index: 10;
        }
        .line {
            position: absolute;
            left: 5px;
            top: 8px;
            width: 4px;
            height: 85px;
            background-color: var(--change-tip-line);
        }
        .tip {
            position: absolute;
            left: 25px;
            top: -4px;
            color: var(--change-font); //#303133
            font-size: 15px;
            font-weight: 500;
            line-height: 23px;
        }
    }
</style>