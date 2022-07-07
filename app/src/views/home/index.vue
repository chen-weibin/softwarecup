<template>
    <div class="main">
        <Header />
        <div class="home">
            <transition appear name="history-occur">
                <History v-show="isshow"/>
            </transition>
            <transition appear name="aside-toright">
                <Aside v-show="isshow"/> 
            </transition>
            <transition appear name="message-occur">
                <Message v-show="isshow"/>
            </transition>
        </div>
    </div>
</template>

<script>
    import Header from '@/components/header/Header.vue'
    import History from '@/components/history/History.vue';
    import Message from '@/components/message/Message.vue';
    import Aside from '@/components/aside/Aside.vue';
    export default {
        name: 'Home',
        components: {
            Header,
            History,
            Message,
            Aside
        },
        data(){
            return {
                isshow: true
            }
        },
        activated(){
            this.isshow = true
        }
    }
</script>

<style scoped lang='less'>
    .main {
        width: 100%;
        height: 100%;
        .home {
            width: 100%;
            height: 88%;
        }
    }
    @keyframes asidetoright {
        0% {
        opacity: 0;
        transform: translateX(-100%);
        }
        100% {
        opacity: 1;
        transform: translateX(0);
        }
    }
    .aside-toright-enter-active {
        animation: asidetoright .8s;
    }
    .aside-toright-leave-active {
        animation: asidetoright .8s reverse;
    }

    @keyframes historyoccue {
        0% {
        opacity: 0;
        transform: translateX(100%);
        }
        100% {
        opacity: 1;
        transform: translateX(0);
        }
    }
    .history-occur-enter-active {
        animation: historyoccue .8s;
    }
    .history-occur-leave-active {
        animation: historyoccue .8s reverse;
    }

    @keyframes messageoccur {
        0% {
        opacity: 0;
        transform: translateY(100%);
        }
        100% {
        opacity: 1;
        transform: translateY(0);
        }
    }
    .message-occur-enter-active {
        animation: asidetoright .8s;
    }
    .message-occur-leave-active {
        animation: messageoccur .8s reverse;
    }
</style>