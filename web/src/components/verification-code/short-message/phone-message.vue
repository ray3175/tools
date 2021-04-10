<template>
    <div>
        <div class="row">
            <div class="col-12">
                <div class="card text-center shadow-lg rounded">
                    <div class="card-header">{{ phone }}</div>
                    <div class="card-body">
                        <h5 class="card-title">{{ message.code }}</h5>
                        <p class="card-text">{{ message.text }}</p>
                    </div>
                    <div class="card-footer text-muted">为避免IP被封，建议每次请求的时间间隔为10秒以上。不再使用的号码，建议及时释放！</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "phone-message",
        props: {
            phone: {
                type: String,
                default: null
            }
        },
        data() {
            return {
                message: {}
            };
        },
        methods: {
            setMessage(message) {
                this.message = message;
            }
        }
    }
</script>

<style scoped>
    .row {
        margin-top: 20px;
    }
</style>
