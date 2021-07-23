import React, {Component} from 'react';

class MyComponent extends Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        categories: []
      }
    }
  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/category/?format=json")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            categories: result
          });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
      handleDelete = catId => (
        fetch('http://127.0.0.1:8000/api/category/' + catId, {method: 'DELETE'}).then((response) => {
        }).then((result) => {
            window.location.reload(false);
        })
      );
  render() {
    const { error, categories } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else {
      return (
          <div class="col-10 offset-1">
            <h1 class="d-inline">Human shop</h1><img class="w-25 h-25 d-inline" src="https://www.pngitem.com/pimgs/m/533-5331872_black-business-people-png-transparent-png.png"/>
            <table>
                <tr class="border text-light bg-dark">
                    <th class="col-1">ID</th><th class="col-2">NAME</th><th class="col-3">GOODS</th><th class="col-3">LAST WORDS</th>
                </tr>
                  {categories.map(category => (
                  <tr class="border" key={category.id}>
                       <td class="col-1">{category.id}
                            <button class="btn btn-primary" id={category.id} onClick={() => {this.handleDelete(category.id)}}>BUY</button>
                       </td>
                       <td class="col-2">{category.name}</td>
                       <td class="col-3"><ul>{category.goods.map(good => (
                           <li>{good.name} ${good.price}</li>
                       ))}</ul>num_of_goods: {category.num_of_goods}</td>
                       <td class="col-3"><ul>{category.tags.map(tag => (
                           <li>{tag.name}</li>
                       ))}</ul>num_of_tags: {category.num_of_tags}</td>
                  </tr>
                  ))}
            </table>
          </div>
      );
    }
  }

  handleDelete(cat_id){
       console.log(cat_id);
  }
}

export default MyComponent;
