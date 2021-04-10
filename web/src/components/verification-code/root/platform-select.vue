<template>
    <div id="select-platform">
        <div v-for="(platformName, index) in platformNameList" class="self-platform-select-div">
            <button @click="$parent.selectPlatform(platformName)" class="btn btn-lg btn-outline-success self-platform-select-button-width" type="button">{{ platformName }}</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'platform-select',
        data() {
            return {
                platformNameList: []
            };
        },
        mounted () {
            this.$parent.getCodePlatformList().forEach((value) => {
                this.platformNameList.push(value.name);
            })
        }
    }
</script>

<style scoped>
    .self-platform-select-div {
        margin-bottom: 15px;
    }

    .self-platform-select-button-width {
        width: 300px;
    }

    #select-platform {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
        align-content: space-around;
    }
</style>
