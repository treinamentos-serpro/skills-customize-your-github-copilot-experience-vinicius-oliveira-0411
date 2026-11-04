from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def main():
    iris = load_iris()
    features = iris.data
    labels = iris.target

    features_train, features_test, labels_train, labels_test = train_test_split(
        features,
        labels,
        test_size=0.25,
        random_state=42,
        stratify=labels,
    )

    print(f"Features: {', '.join(iris.feature_names)}")
    print(f"Classes: {', '.join(iris.target_names)}")
    print(f"Training samples: {len(features_train)}")
    print(f"Test samples: {len(features_test)}")

    model = DecisionTreeClassifier(random_state=42)
    model.fit(features_train, labels_train)
    predictions = model.predict(features_test)

    class_indexes = list(range(len(iris.target_names)))
    print(f"\nBaseline accuracy: {accuracy_score(labels_test, predictions):.2f}")
    print("Baseline confusion matrix:")
    print(confusion_matrix(labels_test, predictions, labels=class_indexes))

    print("\nAccuracy by maximum tree depth:")
    for depth in (1, 2, 3):
        depth_model = DecisionTreeClassifier(max_depth=depth, random_state=42)
        depth_model.fit(features_train, labels_train)
        depth_predictions = depth_model.predict(features_test)
        score = accuracy_score(labels_test, depth_predictions)
        print(f"Depth {depth}: {score:.2f}")


if __name__ == "__main__":
    main()
