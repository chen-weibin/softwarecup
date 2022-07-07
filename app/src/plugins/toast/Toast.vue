<template>
    <transition appear name="show" >
        <div class="show" :style="toastStyle" v-if="isShow">
            <svg-icon :iconClass="icon" className="icon"/>
            {{text}}
        </div>
    </transition>
</template>

<script>
    export default {
        name: 'Toast',
        props: {
            text: {
                type: String,
                default: ''
            },
            type:{
                type: String,
                default: 'success'
            }
        },
        data(){
            return {
                bgc: '#e6f9db', // 背景颜色
                color: 'rgb(0, 196, 29)', // 字体颜色
                border: '1px solid rgb(131, 247, 158)',// 边框
                isShow: false
            }
        },
        computed: {
            toastStyle(){
                return {
                    background: this.bgc,
                    color: this.color,
                    border: this.border
                }
            },
            icon(){
                return this.type
            }
        },
        watch: {
            type: {
                immediate: true,
                handler(){
                    switch(this.type){
                        case 'success':
                            this.bgc = '#e6f9db'
                            this.color = 'rgb(0, 196, 29)'
                            this.border = '1px solid rgb(131, 247, 158)'
                            break
                        case 'warning':
                            this.bgc = '#fce5c6'
                            this.color = 'rgb(228, 147, 5)'
                            this.border = '1px solid rgb(245, 191, 105)'
                            break
                        case 'error':
                            this.bgc = '#fcd3d3'
                            this.color = 'rgb(200, 44, 44)'
                            this.border = '1px solid rgb(249, 118, 118)'
                            break
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .show{
        overflow: hidden;
        position: absolute;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 270px;
        height: 50px;
        border-radius: 6px;
        box-sizing: border-box;
        text-align: center;
        line-height: 50px;
        font-size: 17px;
    }
    .icon {
        height: 25px;
        transform: translateY(-1.5px);
    }
    .show-enter-active{
        animation: appear .4s linear
    }
    .show-leave-active{
        animation: appear .4s linear reverse;
    }
    @keyframes appear {
        0%{
            top: 0;
            opacity: 0;
        }
        100%{
            top: 20px;
            opacity: 1;
        }
    }
    
</style>