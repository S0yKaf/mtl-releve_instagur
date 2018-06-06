let index = new Vue({
  el: '#index',
  name: 'index',
  data: {
    posts: [],
    userComment: ""
  },
  methods: {
    like: function (post) {
      const id = post.id;
      axios.post(`/post/${id}/like`)
      .then((res) => {
        post.likes++;
      })
      .catch((err) => {
        console.log(err);
      })
    },
    comment: function (id, comment) {
      const data = {
        'comment': comment
      }
      axios.post(`/post/${id}/comment`, data)
      .then((res) => {
        window.location.replace('/');
      })
      .catch((err) => {
        console.log(err);
      })
    }
  },
  created: function () {
    axios.get('/post/all')
    .then((res) => {
      this.posts = res.data;
      return Promise.resolve();
    })
    .catch((err) => {
      console.log(err);
    });
  }
})
