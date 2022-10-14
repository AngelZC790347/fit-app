<script>
export default {
    props: ['dni'],
    methods: {
        async getlogin(dni) {
            let user = await fetch(`http://localhost:5000/login`)
            // this.user = await user.json()
            this.currentUser = await user.text()
        },
        async getUser(dni) {
            let user = await fetch(`http://localhost:5000/user/id:${dni}`)
            this.currentUser = await user.json()
        },
    },
    data() {
        return {
            currentUser: 'An',
            auth: false,
        }
    },
    beforeCreate() {
        console.log(this.dni)
    },
    created() {},
    beforeMount() {
        // methods can be called in lifecycle hooks, or other methods!
        // this.getUser(this.dni)
        this.getUser(this.dni)
    },

    mounted() {},

    beforeUpdate() {},

    updated() {},

    beforeUnmount() {},
}
</script>

<template>
    <nav>
        <a href="#/">HomeView</a> 
        | <a href="#/about">About</a> |
        <a href="#/non-existent-path">Broken Link</a>
        <component :is="currentView" />
    </nav>
    <div>
        <h1>{{ currentUser.name }}</h1>
    </div>
</template>
