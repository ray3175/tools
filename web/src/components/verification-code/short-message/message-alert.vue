<template>
    <div :id="'short-message-message-alert-' + phone" class="alert alert-success alert-dismissible fade show" role="alert">
        <slot></slot>
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>
</template>

<script>
    export default {
        name: "message-alert",
        props: ["phone"],
        mounted() {
            setTimeout(() => {
                $("#short-message-message-alert-" + this.phone).alert("close");
            }, 2000);
        }
    }
</script>

<style scoped>

</style>