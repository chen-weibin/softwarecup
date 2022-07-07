<template>
    <div class="theme">
        <div class="main" @click="change" :data-str="str">
            <div class="container" ></div>
            <div class="slider" ref="slider"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Theme',
        data() {
            return {
                root: null, // 保存设置属性值的节点
                theme: 'light', //当前主题
                str: '经典模式', // 提示的信息
            }
        },
        mounted(){
            this.root = document.querySelector(':root')
        },
        methods: {
            change() {
                if (this.theme === 'light') {
                    this.theme = 'dark'
                } else {
                    this.theme = 'light'
                }
            }      
        },
        watch: {
            theme: {
                handler() {
                    // 改变图标的位置 和整个主题
                    const {root} = this
                    if (this.theme === 'light') {
                        this.$refs.slider.style.left = '2px'
                        this.$store.dispatch('changeTheme', 'light')
                        root.style.setProperty('--bgc-start-color', '#e4e4e4');   
                        root.style.setProperty('--bgc-middle-color', '#e4e4e4');   
                        root.style.setProperty('--bgc-end-color', '#e4e4e4'); 
                        
                        root.style.setProperty('--theme-select-color', '#fff'); 
                        root.style.setProperty('--theme-select-slider', '#517fff');  
                        root.style.setProperty('--theme-select-text-color', 'black'); 
                        root.style.setProperty('--theme-select-text-bg-color', 'rgb(241, 241, 241)'); 
                        this.str = '经典模式'

                        root.style.setProperty('--header-bg-color', '#517fff'); 
                        root.style.setProperty('--max-min-screen', 'white'); 
                        
                        root.style.setProperty('--title-color', 'white');
                        
                        root.style.setProperty('--aside-bg-first-color', '#7b9efe');
                        root.style.setProperty('--aside-bg-second-color', '#7b9efe');
                        root.style.setProperty('--aside-bg-third-color', '#7b9efe');
                        root.style.setProperty('--aside-bg-fourth-color', '#7b9efe');
                        root.style.setProperty('--aside-mask-start-color', 'transparent');
                        root.style.setProperty('--aside-mask-end-color', 'transparent');
                        
                        root.style.setProperty('--item-bg-color', '#15CE96');

                        root.style.setProperty('--menu-now-font-color', 'rgb(255, 255, 255)');
                        root.style.setProperty('--menu-now-bg-color', '#08e09f');
                        root.style.setProperty('--menu-bg-color', '#618bfe');
                        root.style.setProperty('--menu-font-color', 'white');            
                        root.style.setProperty('--menu-message-bg-color', '#FFFFFF');
                        root.style.setProperty('--menu-message-title-color', 'black');
                        root.style.setProperty('--menu-message-desc-color', 'black');
                        root.style.setProperty('--menu-message-dian-color', '#08e09f');
                        root.style.setProperty('--menu-tools-bg-color', '#08e09f');
                        root.style.setProperty('--menu-tools-font-color', 'rgb(255, 255, 255)');
                        root.style.setProperty('--memu-border-color', 'transparent');
                        
                        const url = require('@/assets/卫星.png')
                        root.style.setProperty('--information-bg', `white url('${url}') no-repeat 275px 245px`);
                        root.style.setProperty('--information-title-color', 'black');
                        root.style.setProperty('--information-item-color', 'rgb(126, 125, 125)');
                        root.style.setProperty('--information-desc-color', 'black');
                        root.style.setProperty('--information-one-color', 'rgb(107, 255, 122)');
                        root.style.setProperty('--information-two-color', 'rgb(255, 51, 28)');
                        root.style.setProperty('--information-three-color', 'rgb(251, 255, 0)');
                        root.style.setProperty('--information-four-color', 'rgb(76, 210, 255)');
                        root.style.setProperty('--information-five-color', 'rgb(255, 188, 54)');
                        
                        root.style.setProperty('--history-bg', 'white');
                        root.style.setProperty('--history-item-bg-color', '#4de4b6');
                        root.style.setProperty('--history-item-before', 'black');
                        root.style.setProperty('--history-item-label', 'white');
                        root.style.setProperty('--history-item-time', 'black');
                        root.style.setProperty('--history-scroll-track', '#cccccc');
                        root.style.setProperty('--history-scroll-thumb', '#83a4ff');
                        root.style.setProperty('--history-scroll-hover', '#7096ff');

                        root.style.setProperty('--main-bg', 'white');
                        root.style.setProperty('--main-font-color', 'black');
                        
                        root.style.setProperty('--change-bg', `white url('${url}') no-repeat 160px -30px`);
                        root.style.setProperty('--change-ra', 'none');
                        root.style.setProperty('--change-bt', '#13dfa2');
                        root.style.setProperty('--change-tip-circle', '#d7dbe1');
                        root.style.setProperty('--change-tip-line', '#E4E7ED');
                        root.style.setProperty('--change-font', '#4b4c4f');

                        root.style.setProperty('--change-res-border', 'none');
                        
                        root.style.setProperty('--upload-border', '#d9d9d9');
                        root.style.setProperty('--upload-border-hov', '#7B9EFE');
                        root.style.setProperty('--upload-font', '#606266');
                        root.style.setProperty('--upload-tit', '#409eff');

                        root.style.setProperty('--upload-icon', '#C0C4CC');


                        root.style.setProperty('--user-bg-border', '#d1d1d1');
                        root.style.setProperty('--user-bg', 'rgb(254, 253, 254)');
                        root.style.setProperty('--user-touxiang', 'rgb(68, 162, 255)');
                        root.style.setProperty('--user-list-font', 'rgb(42, 42, 42)');
                        root.style.setProperty('--user-show', '#E3E5E7');


                        root.style.setProperty('--scan-color', '#517FFF');
                        root.style.setProperty('--scan-line', 'rgb(0, 255, 166)');
                        root.style.setProperty('--scan-show1', 'linear-gradient(to bottom, rgba(88, 255, 197, .0), rgba(88, 255, 197, .7))');
                        root.style.setProperty('--scan-show2', 'linear-gradient(to top, rgba(88, 255, 197, .0), rgba(88, 255, 197, .7))');
                    



                        

                    } else {
                        this.$refs.slider.style.left = '22px'
                        this.$store.dispatch('changeTheme', 'dark')
                        root.style.setProperty('--bgc-start-color', '#7581a4');   
                        root.style.setProperty('--bgc-middle-color', '#4C5475');   
                        root.style.setProperty('--bgc-end-color', '#242948');   

                        root.style.setProperty('--theme-select-color', '#15d2f3'); 
                        root.style.setProperty('--theme-select-slider', 'white');  
                        root.style.setProperty('--theme-select-text-color', 'white'); 
                        root.style.setProperty('--theme-select-text-bg-color', 'black'); 
                        this.str = '黑暗模式'

                        root.style.setProperty('--header-bg-color', 'transparent'); 
                        root.style.setProperty('--max-min-screen', '#00d8fe'); 

                        root.style.setProperty('--title-color', 'white'); 

                        root.style.setProperty('--aside-bg-first-color', 'rgb(106, 199, 236)');
                        root.style.setProperty('--aside-bg-second-color', '#9b6cfa');
                        root.style.setProperty('--aside-bg-third-color', '#ed725a');
                        root.style.setProperty('--aside-bg-fourth-color', '#64629a');
                        root.style.setProperty('--aside-mask-start-color', 'rgba(255, 255, 255, .2)');
                        root.style.setProperty('--aside-mask-end-color', 'transparent');

                        root.style.setProperty('--item-bg-color', 'transparent');
                        
                        root.style.setProperty('--menu-now-font-color', 'white');
                        root.style.setProperty('--menu-now-bg-color', '#7b3bfd');
                        root.style.setProperty('--menu-bg-color', 'rgb(48, 190, 246)');
                        root.style.setProperty('--menu-font-color', 'white');            
                        root.style.setProperty('--menu-message-bg-color', 'transparent');
                        root.style.setProperty('--menu-message-title-color', 'white');
                        root.style.setProperty('--menu-message-desc-color', 'white');
                        root.style.setProperty('--menu-message-dian-color', '#fdb33b');
                        root.style.setProperty('--menu-tools-bg-color', 'transparent');
                        root.style.setProperty('--menu-tools-font-color', 'rgb(255, 255, 255)');
                        root.style.setProperty('--memu-border-color', '#1B1E2B');
                        
                        root.style.setProperty('--information-bg', `transparent`);
                        root.style.setProperty('--information-title-color', 'white');
                        root.style.setProperty('--information-item-color', 'white');
                        root.style.setProperty('--information-desc-color', 'rgb(235, 235, 235)');
                        root.style.setProperty('--information-one-color', 'rgb(107, 255, 122)');
                        root.style.setProperty('--information-two-color', 'rgb(255, 51, 28)');
                        root.style.setProperty('--information-three-color', 'rgb(251, 255, 0)');
                        root.style.setProperty('--information-four-color', 'rgb(76, 210, 255)');
                        root.style.setProperty('--information-five-color', 'rgb(255, 188, 54)');
                        
                        root.style.setProperty('--history-bg', 'transparent');
                        root.style.setProperty('--history-item-bg-color', '#4f4d76');
                        root.style.setProperty('--history-item-before', 'white');
                        root.style.setProperty('--history-item-label', 'white');
                        root.style.setProperty('--history-item-time', 'rgb(238, 238, 238)');
                        root.style.setProperty('--history-scroll-track', '#525B7C');
                        root.style.setProperty('--history-scroll-thumb', '#7d9df4');
                        root.style.setProperty('--history-scroll-hover', '#6a91fe');

                        root.style.setProperty('--main-bg', 'transparent');
                        root.style.setProperty('--main-font-color', 'white');
                        
                        root.style.setProperty('--change-bg', `transparent`);
                        root.style.setProperty('--change-ra', '8px');
                        root.style.setProperty('--change-bt', '#64629a'); 
                        root.style.setProperty('--change-tip-circle', 'white');
                        root.style.setProperty('--change-tip-line', '#E4E7ED');
                        root.style.setProperty('--change-font', 'white');
                        
                        root.style.setProperty('--change-res-border', '1px solid #1B1E2B');
                        
                        root.style.setProperty('--upload-border', 'white');
                        root.style.setProperty('--upload-border-hov', '#30BEF6');
                        root.style.setProperty('--upload-font', 'white');
                        root.style.setProperty('--upload-tit', 'rgb(4, 242, 255)');
                        root.style.setProperty('--upload-icon', 'white');


                        root.style.setProperty('--user-bg-border', '#5b6481');
                        root.style.setProperty('--user-bg', '#383E5E');
                        root.style.setProperty('--user-touxiang', 'rgb(154, 243, 255)');
                        root.style.setProperty('--user-list-font', 'white');
                        root.style.setProperty('--user-show', '#272C4B');

                        root.style.setProperty('--scan-color', '#00f7ff');  //#00f2ff
                        root.style.setProperty('--scan-line', 'rgb(0, 231, 247)');
                        root.style.setProperty('--scan-show1', 'linear-gradient(to bottom, rgba(88, 255, 197, .0), rgba(23, 240, 255, 0.7))');
                        root.style.setProperty('--scan-show2', 'linear-gradient(to top, rgba(88, 255, 197, .0), rgba(23, 240, 255, 0.7))');
                    

                    }
                    
                }
            }
        }
        
    }
</script>

<style lang='less' scoped>
    .theme {
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .main {
        width: 40px;
        height: 18px;
        border-radius: 9px;
        position: relative; 
        cursor: pointer;      
        &:hover::before {
            display: block;
            position: absolute;
            content: attr(data-str);
            width: 70px;
            top: 25px;
            right: 0px;
            font-size: 14px;
            text-align: center;
            color: var(--theme-select-text-color);
            border-radius: 3px;
            background-color: var(--theme-select-text-bg-color);
        }
        .container{
            width: 40px;
            height: 18px;
            border-radius: 9px;
            background-color: var(--theme-select-color);
        }
        .slider {
            position: absolute;
            width: 15px;
            height: 15px;
            border-radius: 50%;
            left: 1.5px;
            top: 1.5px;
            background-color: var(--theme-select-slider);
            transition: all .3s;

        }
    }
</style>