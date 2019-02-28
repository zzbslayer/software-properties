import React from "react";
// @material-ui/core components
import withStyles from "@material-ui/core/styles/withStyles";
// core components
import GridItem from "components/Grid/GridItem.jsx";
import GridContainer from "components/Grid/GridContainer.jsx";
import Table from "components/Table/Table.jsx";
import Card from "components/Card/Card.jsx";
import CardHeader from "components/Card/CardHeader.jsx";
import CardBody from "components/Card/CardBody.jsx";

const styles = {
  cardCategoryWhite: {
    "&,& a,& a:hover,& a:focus": {
      color: "rgba(255,255,255,.62)",
      margin: "0",
      fontSize: "14px",
      marginTop: "0",
      marginBottom: "0"
    },
    "& a,& a:hover,& a:focus": {
      color: "#FFFFFF"
    }
  },
  cardTitleWhite: {
    color: "#FFFFFF",
    marginTop: "0px",
    minHeight: "auto",
    fontWeight: "300",
    fontFamily: "'Roboto', 'Helvetica', 'Arial', sans-serif",
    marginBottom: "3px",
    textDecoration: "none",
    "& small": {
      color: "#777",
      fontSize: "65%",
      fontWeight: "400",
      lineHeight: "1"
    }
  }
};

function TableList(props) {
  
  const { classes } = props;
  var ori_userdata = props.location.state.userdata; 
  var userData = [];
  var userDataName = ["Check out Time", "Handle", "Server Host", "Port"];
  var item = {};
  for(item in ori_userdata){
    item = ori_userdata[item]
    var singleData = []
    console.log(item)
    singleData.push(item["checkout_time"])
    singleData.push(item["handle"])
    singleData.push(item["server_host"])
    singleData.push(item["port"])
    console.log(singleData)
    userData.push(singleData)
  }

  /*  fetch("http://localhost:5000/status", {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        },
    })
    .then(
        res => res.json()
    )
    .then(
        (result) => {
          //console.log(result['MATLAB']['user_data'])
          //console.log(result["MATLAB"])
          //this.setState({userData: result['MATLAB']['user_data']})
          userData = result['MATLAB']['user_data']
        }
    )//*/

  return (
    <GridContainer>
      <GridItem xs={12} sm={12} md={12}>
        <Card>
          <CardHeader color="primary">
            <h4 className={classes.cardTitleWhite}>User Data</h4>
            <p className={classes.cardCategoryWhite}>
              {props.location.state.name}
            </p>
          </CardHeader>
          <CardBody>
            <Table
              tableHeaderColor="primary"
              tableHead={userDataName}
              tableData={userData}
            />
          </CardBody>
        </Card>
      </GridItem>

    </GridContainer>
  );
}

export default withStyles(styles)(TableList);
