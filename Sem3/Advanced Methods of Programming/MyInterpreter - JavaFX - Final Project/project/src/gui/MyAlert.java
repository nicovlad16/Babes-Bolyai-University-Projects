package gui;


import javafx.scene.control.Alert;


class MyAlert
{
    static void showAlert(String header, String message, String type)
    {
        Alert errorAlert;
        switch (type)
        {
            case "information":
                errorAlert = new Alert(Alert.AlertType.INFORMATION);
                break;
            case "warning":
                errorAlert = new Alert(Alert.AlertType.WARNING);
                break;
            case "confirmation":
                errorAlert = new Alert(Alert.AlertType.CONFIRMATION);
                break;
            case "none":
                errorAlert = new Alert(Alert.AlertType.NONE);
                break;
            default:
                errorAlert = new Alert(Alert.AlertType.ERROR);
                break;
        }

        errorAlert.setHeaderText(header);
        errorAlert.setContentText(message);
        errorAlert.showAndWait();
    }
}
