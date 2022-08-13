import Card from "react-bootstrap/Card";
import "./RecipeView.css";
import { Link } from "react-router-dom";

function RecipeResults(props) {
  return (
    <div className="container">
      <div className="recipeView">
        {props.data.map((singleRecipeData) => (
          <RecipeCard data={singleRecipeData} />
        ))}
        {props.data.length === 0
          ? <SearchError/>
          : null}
      </div>
    </div>
  );
}

export default RecipeResults;

function RecipeCard(props) {
  return (
    <div style={{ display: "inline-block", margin: "1em" }}>
      <div className="recipeCard">
        <Card
          className="recipeCard"
          style={{ width: "16rem", height: "26rem" }}
        >
          <Link
            to={`/recipe-detail/${props.data["Recipe ID"]}`}
            state={props.data}
          >
            <Card.Img variant="top" src={`${props.data["Image URL"]}`} />
          </Link>
          <Card.Body>
            <div className="row">
              <div className="col">
                <Card.Title>{props.data["Name"]}</Card.Title>
              </div>
              <div className="col">
                <Card.Text>⭐️ No Reviews</Card.Text>
              </div>
            </div>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}

function SearchError() {
  return (
    <h2 className="searchError">
      No results found. Please check your spelling and try again.
    </h2>
  )
}