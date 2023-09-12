use tokio::fs;

#[tokio::main]
async fn main() -> Result<(), sqlx::Error> {
    let contents = fs::read_to_string("./usfm/01_Genesis.usfm").await.unwrap();
    return Ok(());
}
