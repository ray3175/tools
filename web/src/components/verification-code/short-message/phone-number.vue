<template>
    <div>
        <div class="row">
            <div class="col-12">
                <div class="list-group shadow-lg rounded">
                    <a v-for="(obj, key, index) in phoneDict" :key="index" :class="key === phone ? 'active' : null" @click="activePhoneNumber(key)" href="javascript:void(0)" class="list-group-item d-flex justify-content-between align-items-center list-group-item-action">
                        {{ key }}
                        <span v-show="obj.unreadInfoNumber" class="badge badge-primary badge-pill">{{ obj.unreadInfoNumber }}</span>
                    </a>
                </div>
            </div>
        </div>
        <div class="row self-end-row"></div>
    </div>
</template>

<script>
    export default {
        name: "phone-number",
        props: {
            phone: {
                type: String,
                default: null
            },
            phoneDict: {
                type: Object,
                default: () => {}
            }
        },
        methods: {
            activePhoneNumber(phone) {
                this.$parent.activePhoneNumber(phone);
            }
        }
    }
</script>

<style scoped>
    .row {
        margin-top: 20px;
    }

    .self-end-row {
        margin-bottom: 20px;
    }
</style>
