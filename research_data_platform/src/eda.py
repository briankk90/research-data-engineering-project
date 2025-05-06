import pandas as pd
import seaborn as sns
import plotly.express as px
from src.utils import setup_logger

logger = setup_logger('eda')

def perform_eda(df, output_dir):
    """Perform exploratory data analysis."""
    try:
        # Summary statistics
        summary = df.describe()
        summary.to_csv(f"{output_dir}/summary_stats.csv")
        
        # Correlation heatmap
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.savefig(f"{output_dir}/correlation_heatmap.png")
        
        # Interactive scatter plot
        fig = px.scatter(df, x='feature1', y='feature2', color='category')
        fig.write(f"{output_dir}/scatter_plot.html")
        
        logger.info("EDA completed")
    except Exception as e:
        logger.error(f"Error in EDA: {e}")
        raise