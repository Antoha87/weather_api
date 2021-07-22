import React, {Component} from 'react';

class MyComponent extends Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        goods: []
      }
    }
  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/goods/?format=json")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            goods: result
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

  render() {
    const { error, goods } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else {
      return (
          <div class="col-8 offset-2">
            <h1 class="d-inline">Goods list</h1><img class="w-25 h-25 d-inline" src="https://www.pngitem.com/pimgs/m/533-5331872_black-business-people-png-transparent-png.png"/>
            <table>
                <tr class="border text-light bg-dark">
                    <th class="col-3">ID</th><th class="col-3">NAME</th><th class="col-3">PRICE</th>
                </tr>
                  {goods.map(good => (
                  <tr class="border" key={good.id}>
                       <td class="col-3">{good.id}</td><td class="col-3 bg-primary text-white">{good.name}</td><td class="col-3 text-success bg-warning">£{good.price}</td>
                  </tr>
                  ))}
            </table>
          </div>
      );
    }
  }
}

export default MyComponent;
