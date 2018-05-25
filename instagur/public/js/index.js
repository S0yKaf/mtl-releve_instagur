let index = new Vue({
  el: '#index',
  name: 'index',
  data: {
    posts: {}
  },
  methods: {
  },
  beforeCreate: function () {
    axios.get('/post/all')
    .then((res) => {
      this.posts = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
  }
})
