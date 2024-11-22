# check if kaggle package is installed
if ! command -v kaggle &> /dev/null
then
    echo "kaggle package could not be found"
    echo "Install kaggle package"
    pip install kaggle
fi

# copy the kaggle.json file to the ~/.kaggle/
mkdir -p ~/.kaggle
cp script/kaggle.json ~/.kaggle/

# download the dataset
kaggle competitions download -c jane-street-real-time-market-data-forecasting

# unzip the dataset (create the dataset folder if it does not exist)
unzip jane-street-real-time-market-data-forecasting.zip -d dataset